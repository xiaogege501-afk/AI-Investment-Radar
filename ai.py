import os
import requests



MODEL = (
"https://api-inference.huggingface.co/models/"
"Qwen/Qwen2.5-7B-Instruct"
)



def generate_report(data):


    api_key=os.getenv(
        "HUGGINGFACE_API_KEY"
    )


    if not api_key:

        return (
            "AI模型未连接，"
            "当前使用量化评分。"
        )


    headers={

        "Authorization":
        f"Bearer {api_key}"

    }


    prompt=f"""

你是一名金融市场分析助手。

根据以下数据生成简短市场分析：

{data}


要求：

1. 不预测未来价格

2. 给出上涨原因

3. 给出风险提醒

4. 给出观察建议


使用中文回答。

"""


    response=requests.post(

        MODEL,

        headers=headers,

        json={

            "inputs":prompt

        },

        timeout=30

    )


    result=response.json()


    if isinstance(result,list):

        return result[0]["generated_text"]


    return "AI暂时无法生成分析"
