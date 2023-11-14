import openai
import streamlit as st
from .prompt import *
import os
import time

#
# Call OPENAI GPT-3 to generate the response
#
def cosmic_analyze(uc_name, uc_content):

    api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = api_key
    start = time.time()
    uc_content_s = split_sentences(uc_content)
    print("DOPO split solo di content")
    print(uc_content_s)
    lines = "FP \"" + uc_name+"\":\n"+uc_content_s+"\n\nFP: \""+uc_name+"\" measurement:"
    print(lines)
    timeout = 5

    while True:
        try:
            response = openai.ChatCompletion.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": SYSTEM_COSMIC_MEASURE},
                                {"role": "user", "content": lines}
                            ],
                            temperature=0
                        )
            res = response['choices'][0]['message']['content']

            print(res)
            st.session_state["analysis"] = res
            break
        except Exception as e:
            st.write('There was an error =('+str(e)+')')
            time.sleep(timeout)
            timeout = timeout *2
    end = time.time()

    print("TIME:",end-start)

#
# split the use case content in atomic sentences
#
def split_sentences(sentences):

    while(sentences.startswith("\n")):
        #print("rimuovo un initial return")
        sentences = sentences[1:len(sentences)]
    
    while(sentences.endswith("\n")):
        #print("rimuovo un trailer return")
        sentences = sentences[0:len(sentences)-1]

    #print(sentences)
    lines = sentences
   
    print(SYSTEM_SPLIT_UC)
    print("=========> DA PRE-SPLIT")
    print(USER_SPLIT.format(uc=lines))
    print("=========> FINE PRE-SPlIT")

    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": SYSTEM_SPLIT_UC},
                            {"role": "user", "content": USER_SPLIT.format(uc=lines)}
                        ],
                        temperature=0
                    )
    res = response['choices'][0]['message']['content']

    return res

#
# PRINT the COSMIC Analysis in a table
#
def print_analysis(lines):

    # Initialize table
    table = {}
    table["FU"] =[]
    table["Sub-process"] =[]
    table["DG"] =[]
    table["OOI"] =[]
    table["DM"] =[]
    table["CFP"] =[]
    subProcess=""
    cont =0
    messages = 0
    isMsg = False
    total = 0
    k = 0
    if( len(lines)>3):
        if(len(lines[0].lstrip()) == 0):
            lines.remove(0)

    if len(lines) >3 and lines[0].startswith('Triggering Event: '):
        st.subheader(lines[0])
        st.subheader(lines[1])
        st.subheader(lines[2])
        lines_r = lines[3:len(lines)]
    else:
        lines_r = lines
    # Parsing GPT-3 response lines
    for i in lines_r:
        l = parseGPTResponse(i)
        # If the error/conf messages has been already counted, we must exclude it
        if i.endswith('Exit. It must be counted only once.'):
            messages = messages +1
            isMsg = True

        if len(l[3])>0:
            table["FU"].append(l[0])
            table["Sub-process"].append(subProcess)
            table["DG"].append(l[1])
            table["OOI"].append(l[2])
            table["DM"].append(l[3])
            if len(l[1])>0:
                if isMsg:
                    if messages <2:
                        table["CFP"].append("1")   
                        total = total+1 
                    else:
                        table["CFP"].append("0")
                else:    
                    table["CFP"].append("1")
                    total = total +1
            else:
                table["CFP"].append("0")    
            cont = 0    
        else:
            if cont == 1:
                table["FU"].append("")
                table["Sub-process"].append(subProcess)
                table["DG"].append("")
                table["OOI"].append("")
                table["DM"].append("")
                table["CFP"].append("")
            subProcess=i    
            cont = 1
    
    table["FU"].append("")
    table["Sub-process"].append("")
    table["DG"].append("")
    table["OOI"].append("")
    table["DM"].append("TOTAL")
    table["CFP"].append(str(total))
    st.table(table)
    #st.markdown(html_code)

#
# Parse a single GPT-Response line
#
def parseGPTResponse(res):
    FU =""
    DG ="" 
    OOI ="" 
    DM =""
    res = res.lstrip()
    if(res.startswith('FU (')):
        try:
            i = res.find(')') # era index
            FU = res[4:i]
            j = res.find("DG (")
            if( j < 0):
                print("DG non trovato")
            i = res.find(')',j)
            if( i < 0):
                print("prima ) non trovata")
            DG = res[j+4:i]
            j = res.find("OOI (")
            if( j < 0):
                print("OOI non trovato")
            i = res.find(')',j)
            if( i < 0):
                print("seconda ) non trovata")
            OOI = res[j+5:i]
            #j = res.find(") - ",j)
            j = i
              
            i = res.find('.',j)
            if( i < 0):
                print(". trovato")
            DM = res[j+4:i]
            if(DM.startswith('D')):
                DM = 'Write'
        except Exception as e:
            st.write('There was an error =('+str(e)+')')
            print(res)
    elif res.startswith('DG ('):
        try:
            j = res.find("DG (")
            i = res.find(')',j)
            DG = res[j+4:i]
            j = res.find("OOI (")
            i = res.find(')',j)
            OOI = res[j+5:i]
            j = res.find(") - ",j)
            i = res.find('.',j)
            DM = res[j+4:i]
            if(DM.startswith('D')):
                DM = 'Write'
        except Exception as e:
            st.write('There was an error =('+str(e)+')')
            print(res)
    elif res.startswith('No data movement.'):
            DM = "No data movement"    
    return [FU, DG, OOI, DM]