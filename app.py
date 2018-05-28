# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:11:50 2018

@author: khimmee
"""

from flask import Flask, request
import json
import requests
import random
listanswer = []
question = ''
face = ''
score = 0
sc = 0
qe = ''
faceqe = ''
appe = []
qqq2 =[]
q2q = ''
scc = 0
i=0 
questionnine = ''
testttt = ''
number1 = ''
evaluation_form ={}
numberaa = ['0','1','2','3']
sayhi = open("sayhi.txt",encoding='utf-8-sig')
sayhi = sayhi.read().split(',')
answer = open("answer.txt","r",encoding='utf-8-sig')
answer = answer.read().split(',')
ques = open("Ques.txt","r",encoding='utf-8-sig')
ques = ques.read().split(',')
quest9 = open("Quest9.txt","r",encoding='utf-8-sig')
quest9 = quest9.read().split(',')
wordappende = open("wordappende.txt","r",encoding='utf-8-sig')
wordappende = wordappende.read().split(',')
qq2 = open("qq2.txt","r",encoding='utf-8-sig')
qq2 = qq2.read().split(',')
evaluation_form['eval'] ={'greet': sayhi,
                         'answer': answer,
                         'ques': ques,
                         'quest9': quest9,
                         'wordap': wordappende,
                         'qq2': qq2,
                         'number': number}
answer0123 = {}
answer0123['answer0123']={'answer0' : 'ไม่มีเลย',
                         'answer1' : 'เป็นบางวัน',
                         'answer2' : 'เป็นบ่อย',
                         'answer3' : 'เป็นทุกวัน'}
select2 = {}
select2['selc'] = {'selc01': 'มี',
                  'selc02' : 'ไม่มี'}
                  
please = {}
please['ple'] = {'ple':'จิ้มที่เเป้นพิมพ์ 0 1 2 3 ตามระดับของอาการที่เป็นหน่อยน้าาา',
                 'ple1':'พิมพ์ "มี" หน่อยนะถ้ามีอาการ พิมพ์ "ไม่มี" ถ้าไม่มีอาการน้าาา',
                 'ple2' :'กรุณาตอบ "ไม่มี" ถ้าไม่มีอาการ หรือตอบ "มี" ถ้าไม่มีอาการ',
                 'ple3': 'กรุณาตอบ "ได้" หากสามารถควบคุมอารมณ์ตัวเองได้ ตอบ "ไม่ไ้ด้" หากท่านไม่สามารถควบคุมอารมณ์ตนเองได้',
                 'Error' : '-- เอ๊ะ! พิมพ์ผิดหรือเปล่าน้าาาา กอดอุ่นไม่เห็นเข้าใจเลย :/'}
setscoreq9 = {}
setscoreq9['score'] = {'pprint' : '0 = ไม่มีเลย\n' + '1 = เป็นบางวัน\n'+ '2 = เป็นบ่อย\n'+ '3 = เป็นทุกวัน\n'}
quest8 = {}
quest8['quest8'] = {'quest01':'มีความคิดอยากตาย หรือคิดว่าตายไปจะดีกว่า',
       'quest02':'อยากทำร้ายตัวเอง หรือทำให้ตัวเองบาดเจ็บ',
       'quest03':'มีความคิดเกี่ยวกับการฆ่าตัวตาย',
       'quest031':'ท่านสามารถควบคุมความอยากฆ่าตัวตายที่ท่านคิดอยู่นั้นได้หรือไม่ หรือบอกได้ไหมว่าคงจะไม่ทำตามความคิดนั้นในขณะนี้',
       'quest04':'มีแผนการที่จะฆ่าตัวตาย',
       'quest05':'ได้เตรียมการที่จะทำร้ายตนเอง หรือเตรียมการจะฆ่าตัวตาย โดยตั้งใจว่าจะให้ตายจริงๆ',
       'quest06':'ได้ทำให้ตนเองบาดเจ็บ แต่ไม่ตั้งใจที่จะทำให้เสียชีวิต',
       'quest07':'ได้พยายามฆ่าตัวตาย โดยคาดหวัง/ตั้งใจที่จะให้ตาย',
       'quest08':'ตลอดชีวิตที่ผ่านมา... ท่านเคยพยายามฆ่าตัวตาย'}
ans8 = {}
ans8['ans'] = {'an' :'ไม่ได้',
               'ay' : 'ได้'}

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer IzXs2WdxBaxjM/BTdVQ43pEYgt1O8BRRrEAOztjHPMfRUmM0BYtD4VRZg7MLMSyi1mWqI3vdPl08HfmsCUiBM1QJKc0OF89EfbEPIHEG+pKHO85//3Zvo+Qcf9MDZoFwe2m+cjasnyvwYZ3xPQNWPgdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
@app.route('/')
def index():
    return 'This is chatbot server.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    
    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID =  msg_in_json["events"][0]['source']['userId']
    msgType =  msg_in_json["events"][0]['message']['type']
    
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    if msgType != 'text':
        reply(replyToken, ['Only text is allowed.'])
        return 'OK',200
    
    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ 
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    
  #########################################################################################################
    if text in evaluation_form['eval']['greet']:
         replyQueue.append(random.choice(evaluation_form['eval']['answer']))
    elif text in evaluation_form['eval']['ques'] or numberaa :
         replyQueue.append(que(text))
         
         ########เรียกใช้ฟังก์ชันข้างล่าง########    
        
            

                
    else:
         replyQueue.append('ไม่รู้ว่าจะตอบอะไรดี TT')
  ##########################################################################################################
  
       
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ non-exact match
    # โดยที่มี method ชื่อ find_closest_sentence ที่ใช้การเปรียบเทียบประโยค
    # เพื่อค้นหาประโยคที่ใกล้เคียงที่สุด อาจใช้เรื่องของ word embedding มาใช้งานได้ครับ
    # simple sentence embeddings --> https://openreview.net/pdf?id=SyK00v5xx
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # closest = find_closest_sentence(response_dict, text)
    # replyQueue.append(reponse_dict[closest])
   
    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    #replyQueue.append('นี่คือรูปแบบข้อความที่รับส่ง')
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    #replyQueue.append(msg_in_string)
    reply(replyToken, replyQueue[:5])
    
    return 'OK', 200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

def que(text):
    if text in evaluation_form['eval']['greet'] :
            print('--' + random.choice(evaluation_form['eval']['answer'] ))
  
    elif text in evaluation_form['eval']['ques']  :
            for j in evaluation_form['eval']['quest9'] :
                if question != listanswer:
                    question = random.choice(evaluation_form['eval']['quest9'])
                    face = random.choice(evaluation_form['eval']['wordap'])
                    listanswer.append(question)
                    print(face+question)
                    print(setscoreq9['score']['pprint'])
                    print(please['ple']['ple'])
                    #print(len(d))
                    n = int(input())
                    nn = n
                    score = score + nn
                    i+=1
                    if i == 9:
                            print(score)
                            i=0
                            #break
                            for h in evaluation_form['eval']['qq2']:
                                if q2q != qqq2:
                                    q2q = random.choice(qq2)
                                    qqq2.append(qq2)
                                    print(q2q)
                                    print(please['ple']['ple1'])
                                    aq2 = input()
                                    if aq2 == select2['selc']['selc01']:
                                        sc+=1
                                        i+=1
                                    elif aq2 == select2['selc']['selc02']:
                                        sc+=0
                                        i+=1
                                        if i==2:
                                            print(sc)
                                            #break
                            
                                            print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest01'])
                                            print(please['ple']['ple2'])
                                            input1 = input()
                                            if input1 == select2['selc']['selc02']:
                                                scc = 0 + scc
                                            else:
                                                scc = 1 + scc
                                                print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest02'])
                                                print(please['ple']['ple2'])
                                            input2 = input()
                                            if input2== select2['selc']['selc02']:
                                                scc = 0+scc
                                            else:
                                                scc = 2+scc
                                    
                                            print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest03'])
                                            print(please['ple']['ple2'])
                                            input3 = input()
                                            if input3 == select2['selc']['selc02']:
                                                scc = 0+scc
                                            else:
                                                scc = 6+scc
                                                print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest031'])
                                                print(lease['ple']['ple3'])
                                            input31 = input()
                                            if input31 == ans8['ans']['ay']:
                                                scc = scc + 0
                                            else:
                                                scc = scc + 8
                                            print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest04'])
                                            print(please['ple']['ple3'])
                                            input4 = input()
                                            if input4 == ans8['ans']['ay']:
                                                scc = scc + 0
                                            else:
                                                scc = scc + 8
                                            print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest05'])
                                            print(please['ple']['ple3'])
                                            input5 = input()
                                            if input5 == ans8['ans']['ay']:
                                                scc = scc + 0
                                            else:
                                                scc = scc + 9
                                            print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest06'])
                                            print(please['ple']['ple3'])
                                            input6 = input()
                                            if input6 == ans8['ans']['ay']:
                                                scc = scc + 0
                                            else:
                                                scc = scc + 4
                                            print(random.choice(evaluation_form['eval']['wordap'])+ quest8['quest8']['quest07'])
                                            print(please['ple']['ple3'])
                                            input7 = input()
                                            if input7 == ans8['ans']['ay']:
                                                scc = scc + 0
                                            else:
                                                scc = scc + 10
                                            print(quest8['quest8']['quest01'])
                                            print(please['ple']['ple3'])
                                            input8 = input()
                                            if input8 == ans8['ans']['ay']:
                                                scc = scc + 0
                                            else:
                                                scc = scc + 4
                                            #scc = input1 + input2 + input3 + input4 + input5 + input6 + input7 + input8
                                            print(scc)
                                            #print(sc)
                                            continue


    




if __name__ == '__main__':
    app.run()
