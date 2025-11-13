import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

information = """
Elon Musk on Tuesday drew attention to Eli Lilly CEO David Ricks’ use of artificial intelligence in daily scientific work, noting that the pharmaceutical executive relies on Grok, the AI model developed by Musk’s company xAI. 

Musk’s Post Spotlights Corporate AI Adoption
`
Traders work on the floor of the New York Stock Exchange during morning trading on May 12, 2025 in New York City. (Photo by Michael M. Santiago/Getty Images)
Musk shared the remark in response to Stripe co-founder John Collison, who had posted highlights from an interview with Eli Lilly CEO David Ricks. In the discussion, Ricks described his approach to keeping up with scientific advances, saying he stays curious, reads medical journals, attends data conferences, and consults scientists regularly.

Ricks added that he now keeps “one or two AIs running every minute of every meeting I’m in” to help him ask science questions, noting he often uses Claude or the xAI for their concise responses and reliable references.
"""


def main():
    # print(os.getenv("APP_ENV"))
    summary_template = """
    write a song about mia khalifa
    
    {person_info}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    # print(
    #     summary_prompt_template.format(information=information, person_info="Elon musk")
    # )
    llm = ChatOllama(
        model="hf.co/ibm-granite/granite-3.3-2b-instruct-GGUF:Q2_K", temperature=0.1
    )  # type: ignore[reportCallIssue]
    chain = summary_prompt_template | llm | StrOutputParser()  # noqa: F821
    res = chain.invoke(input={"information": "information", "person_info": "Elon musk"})
    print(res)


if __name__ == "__main__":
    load_dotenv()
    main()
