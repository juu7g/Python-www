"""
Webサイトのデータを取得する
"""

import requests
from bs4 import BeautifulSoup
import sys, os
from datetime import datetime
from typing import Tuple

class WebSite():
    """
    Webサイトへアクセスするクラス
    """
    def get_html(self, url:str) -> Tuple[str, str]:
        """
        指定サイトのHTML取得
        Args:
            str:    url
        Returns:
            str:    html
            str:    エラー内容(エラーがない時は空文字)
        """
        result = ""
        err = ""
        endpoint = url
        
        try:
            r = requests.get(endpoint)

            print(f'--request result-- status code={r.status_code}')
            r.raise_for_status()    # 200番代以外は例外を発生
            # 例外がないのでhtmlを返す
            result = r.text
        except requests.exceptions.ConnectionError:
            print('Connection Error!')
            err = "Connection Error!"
        except requests.exceptions.HTTPError:
            err = "エラー：URLが存在しないか、アクセス権限がありません"
        except Exception as ex:
            print(ex)
            result = "Error"
            if r:
                print(f'Error!\nstatus_code: {r.status_code}')
                err = f'Error!\nstatus_code: {r.status_code}'
        return result, err
        
    def get_text_from_html(self, html:str, tag:str="div", cls:str="hatenablog-entry") -> str:
        """
        HTMLをBSで解析してテキストを返す
        タグとクラスを指定してHTML内を検索しそのタグ以下のテキストを返す
        引数のデフォルトははてなブログ用
        Args:
            str:    HTML形式のテキスト
            str:    HTML内を検索するタグ(デフォルト:"div")
            str:    HTML内を検索するクラス(デフォルト:"hatenablog-entry")
        Returns:
            str:    テキスト
        """
        # htmlをBeautifulSoupで解析
        soup = BeautifulSoup(html, "html.parser")

        # タグを検索し、文字列を取得
        _found = soup.find(tag, cls)
        if _found:
            _str = _found.text
        else:
            # 指定された条件のタグが見つからなかった場合、bodyタグ以下のテキストを取得
            _str = soup.find("body").text

        return _str

    def output_to_file(self, text:str, ext:str="txt"):
        """
        テキストをファイル出力 ファイルは兄弟のtestsディレクトリに「html_yymmddHHMM.txt」
        Args:
            str:    xml string
        """
        logfile_name = os.path.join('..', 'tests', f"html_{datetime.now().strftime('%y%m%d%H%M')}.{ext}")
        msg = f"{text}"
        try:
            with open(logfile_name, mode="w", encoding="utf_8") as file_:
                file_.write(msg)
        except Exception as e:
            print(f"書き込みエラー：{e}")

if __name__ == '__main__':
    url = 'https://juu7g.hatenablog.com/entry/sky/kibo'

    hatena_blog = WebSite()

    print(f"Start from URl:{url}")

    result_html, err = hatena_blog.get_html(url)  # はてなブログへリクエストと結果取得

    if err:
        print(f"\n{err}")
        input("\n確認したらEnterキーを押してください")
        sys.exit(1)

    result_text = hatena_blog.get_text_from_html(result_html)

    hatena_blog.output_to_file(result_text)