import openai
import streamlit as st

#
# Call OPENAI GPT-3 to generate the response
#
def cosmic_analyze(uc_name, uc_content):
    filename = './cinstructions.txt'
    file = open(filename, 'r')
    lines = file.read()
    file.close()
    uc_content_s = split_sentences(uc_content)
    print("FP \"" + uc_name+"\":\n"+uc_content_s+"\n\nFP: \""+uc_name+"\" measurement:\n")
    lines = lines + "FP \"" + uc_name+"\"\n"+uc_content_s+"\n\nFP: \""+uc_name+"\" measurement:\n"

    #print(lines)

    try:
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt=lines,
            temperature=.5,
            max_tokens=1300,
        )
        print(res)
        st.session_state["analysis"] = res["choices"][0]["text"]

    except Exception as e:
        st.write('There was an error =('+str(e)+')')

#
# split the use case content in atomic sentences
#
def split_sentences(sentences):
    filename = './sinstructions.txt'
    file = open(filename, 'r')
    lines = file.read()
    file.close()
    lines = lines +sentences+"\n"
   
    res = openai.Completion.create(
            model="text-davinci-003",
            prompt=lines,
            temperature=.7,
            max_tokens=1300,
        )

    return res["choices"][0]["text"]

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
        i = res.index(')')
        FU = res[4:i]
        j = res.index("DG (")
        i = res.index(')',j)
        DG = res[j+4:i]
        j = res.index("OOI (")
        i = res.index(')',j)
        OOI = res[j+5:i]
        j = res.index(") - ",j)
        i = res.index('.',j)
        DM = res[j+4:i]

    elif res.startswith('DG ('):
            j = res.index("DG (")
            i = res.index(')',j)
            DG = res[j+4:i]
            j = res.index("OOI (")
            i = res.index(')',j)
            OOI = res[j+5:i]
            j = res.index(") - ",j)
            i = res.index('.',j)
            DM = res[j+4:i]
    elif res.startswith('No data movement.'):
            DM = "No data movement"    
    return [FU, DG, OOI, DM]
