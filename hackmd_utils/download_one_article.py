from pprint import pprint
from datetime import datetime
import pytz
import yaml
import re
import os
from dotenv import load_dotenv
from PyHackMD import API
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def parse_content_yaml(content) -> tuple[dict, str]:
    """
    解析 content 中的 YAML front matter 並返回 (YAML 資料, 剩餘內容)
    """
    if not content.startswith("---\n"):
        logging.warning("無法找到 YAML front matter，返回原始內容")
        return {}, content
    try:
        # 尋找第一個 --- 和第二個 --- 之間的內容
        yaml_end = content.find("\n---\n", 4)  # 從第4個字符開始找第二個 ---
        if yaml_end == -1:
            logging.warning("無法找到結束的 YAML front matter，返回原始內容")
            return {}, content  # 找不到結束的 ---，返回原始內容
        yaml_content = content[4:yaml_end].strip()
        remaining_content = content[yaml_end + 5:].strip()
        # 解析 YAML
        yaml_data = yaml.safe_load(yaml_content) or {}
        return yaml_data, remaining_content
    except yaml.YAMLError:
        logging.warning("無法解析 content 中的 YAML，返回原始內容")
        return {}, content

def remove_top_level_heading(content: str) -> str:
    """
    移除 Markdown 內容開頭的一級標題（# 標題）及其後的換行
    """
    if not content:
        return content
    # 使用正則表達式移除開頭的 # 標題及其後的空行
    cleaned_content = re.sub(r'^# .*\n+', '', content, count=1, flags=re.MULTILINE)
    return cleaned_content

def timestamp_to_iso8601(timestamp_ms) -> str:
    """
    將毫秒時間戳轉換為 ISO 8601 格式（帶台灣時區）
    """
    # 定義台灣時區
    TAIPEI_TZ = pytz.timezone("Asia/Taipei")
    if not timestamp_ms:
        return datetime.now(TAIPEI_TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    dt = datetime.fromtimestamp(timestamp_ms / 1000, tz=pytz.UTC)
    dt_taipei = dt.astimezone(TAIPEI_TZ)
    return dt_taipei.strftime("%Y-%m-%dT%H:%M:%S+08:00")

def convert_info_to_admonition(content):
    """
    將 HackMD 的 強調色塊轉換為 Hugo LoveIt 的 admonition 短碼
    """
    # 正則表達式匹配強調色塊
    pattern = r':::(info|success|warning|danger|spoiler)\n(.*?)\n:::'
    
    def replacement(match):
        block_type = match.group(1)  # 區塊類型（info, warning 等）
        block_content = match.group(2).strip()  # 區塊內容（保留所有內容）

        # 直接使用全部內容，不提取 title
        if block_type == "spoiler":
            return f'{{{{< admonition type=example title="詳細資料" open=false >}}}}\n{block_content}\n{{{{< /admonition >}}}}'
        else:
            return f'{{{{< admonition type={block_type} title="" open=true >}}}}\n{block_content}\n{{{{< /admonition >}}}}'
    
    # 使用正則表達式替換所有強調色塊
    converted_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    return converted_content

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
api = API(API_TOKEN)

# 下載完整內容
note = api.get_note("XLWOQCR9SdWtaXlZE-wkow")
logging.debug(note)

# 解析 content 中的 YAML 和剩餘內容
content_yaml, content_body = parse_content_yaml(note.get("content", ""))

# 移除頂級標題
cleaned_content = remove_top_level_heading(content_body)

# 轉換筆記內容中的強調色塊成 LoveIt 支援的 admonition extended-shortcodes
converted_content = convert_info_to_admonition(cleaned_content)

# 定義新的 YAML front matter
front_matter = {
    "title": note.get("title", "未命名筆記"),
    "date": timestamp_to_iso8601(note.get("createdAt")),        # 將時間戳轉換為 ISO 8601 格式
    "lastmod": timestamp_to_iso8601(note.get("lastChangedAt")), # 將時間戳轉換為 ISO 8601 格式
    "categories": [note["tags"][0]] if note.get("tags") else ["未分類"],
    "tags": note.get("tags", []),
    "featuredImage": content_yaml.get("featuredImage", ""),
    "featuredImagePreview": content_yaml.get("featuredImagePreview", "")
}
front_matter_yaml = yaml.dump(front_matter, allow_unicode=True, sort_keys=False, indent=2)

# 定義檔案路徑
safe_tag = note["tags"][0] if note.get("tags") else "uncategorized"
safe_permalink = note.get("permalink", note.get("id", "unnamed")).replace("/", "_")
file_path = f"content/posts/zh-tw/{safe_tag}/{safe_permalink}.md"

# 取得目錄路徑並創建
directory = os.path.dirname(file_path)
if directory:
    os.makedirs(directory, exist_ok=True)

# 寫入筆記內容
with open(file_path, "w", encoding="utf-8") as file:
    content = f"---\n{front_matter_yaml}---\n\n{converted_content}"
    file.write(content)
logging.info(f"筆記已成功保存至 {file_path}。 筆記標題：'{note['title']}'")

