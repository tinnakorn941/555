# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

cl = LINETCR.LINE() #Luffy
cl.login(token="Ep7qQ6YYPPR7RRYrYzQf.r4b3yRCyjTgcAMdZ+lMGhW.Oj3EcZDibMUYHKj6CusxAn0cdCWl0wyoM0fm99RJcc4=")
cl.loginResult()



ks = kc = kk = ki = cl

print "login By DanaiBot"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║ ✰ 💮_ⓓⓐⓝⓐⓘ_💮 ✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╔═══════════════════
╠     for admin ✍✍️
╠❂͜͡➣ Adminlist
╠❂͜͡➣ Ownerlist
╠❂͜͡➣ Info Group
╠❂͜͡➣ Welcome
╠❂͜͡➣ Creator
╠❂͜͡➣ Bot
╠❂͜͡➣ Cancel
╠❂͜͡➣ 「Buka/Tutup」qr
╠❂͜͡➣ Mid Bot
╠❂͜͡➣ Speed/Sp
╠❂͜͡➣ 「Cctv/Ciduk
╠❂͜͡➣ Status/Set
╠❂͜͡➣ Gurl
╠❂͜͡➣ Jam「On/Off
╠❂͜͡➣ Tag all/Tagall
╠❂͜͡➣ Absen/Respon
╠❂͜͡➣ Banlist
╠❂͜͡➣ Kickall
╚═══════════════════

-==================-
    ✈✈  Ľ¡Ŋ₤βΦŦ  ✈✈
-==================-
"""
KAC=[cl,ki,kk,kc,ks]
#DEF1=[ki,kk,kc,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF2=[cl,kk,kc,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF3=[cl,ki,kc,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF4=[cl,ki,kk,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF5=[cl,ki,kk,kc,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF6=[cl,ki,kk,kc,ks,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF7=[cl,ki,kk,kc,ks,ka,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF8=[cl,ki,kk,kc,ks,ka,kb,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF9=[cl,ki,kk,kc,ks,ka,kb,ko,ku] Udah Ga Kepake(Boleh di apus)
#DEF10=[cl,ki,kk,kc,ks,ka,kb,ko,ke] Udah Ga Kepake(Boleh di apus)
mid = cl.getProfile().mid #Luffy
Amid = ki.getProfile().mid #Zorro
Bmid = kk.getProfile().mid #Sanji
Cmid = kc.getProfile().mid #Ussop
Dmid = ks.getProfile().mid #Chooper

Bots=[mid,Amid,Bmid,Cmid,Dmid]

owner=["ub3db3cc8a5db36da5186eb52d14bfaa9","udb9d815815cf1ad6434275ce27fc2ac0"]
whitelist=["ub3db3cc8a5db36da5186eb52d14bfaa9","ub3db3cc8a5db36da5186eb52d14bfaa9","uc3f34b21479314698c13d8cb72feb28f","u112f0761efc7b9727702039fbe02f574"]
#admin=["ub3db3cc8a5db36da5186eb52d14bfaa9"]
admin=["ub3db3cc8a5db36da5186eb52d14bfaa9","udb9d815815cf1ad6434275ce27fc2ac0","ub3db3cc8a5db36da5186eb52d14bfaa9","u112f0761efc7b9727702039fbe02f574","uc3f34b21479314698c13d8cb72feb28f","udb9d815815cf1ad6434275ce27fc2ac0","uf0d90325e54613d259365b303e115885","u4f8709f6222b794c1f03e7e04ea20277","u531f68025e1b287f71b64588a8b11875","u9dd23f96c172505900d67c03a0166225","u4d23595b08e9f80735739d28392955b0","u08974398f920148a8c62de1f13d97c35","ua16528da89d103b1327f793f5d7e4891","u693bdde4e0393bee2ff85e8562234b09","u7ad11ac73ff71349a735bf8e2ab4664c","u623c1945cdb470707ccdd8ce2de566d1","u6341911d93b68dd732f58e4e9957a885","uefc06d1072eff49d649b64248c221937","ue0c8b2d252076dbf2bd5b04aa5ac8219","ueaf754f4926665b7014585b770e1c04e","ub3d561a2c32242e74f2cd53b4d72da29","u70d4cd257fd6c54009969ca097e5899b","u5d8a47170a059754cb41a02ad21e4454","u5d9711ee93f234533ec493465bbf6fc4","ufb07b944f4c43f321e5dd0896c392730","u9ff50c2181b01db6f261f793a89ed41f","u43ef1454649973b33fc235359b840ff6","ud31d04514d015b4b934f092dd512e51d","uf3dd02b2150a3f5406329fe2a807a589","ua28231315c70dee670e39cd792d1338b","u31d6efccbdff06d624471063c3074d32","u450b768d4238a4dc80b8898aaeafa2c2","u8d503549cead54b326e68ee191fc18aa","uc4567626d83438660047751c2308ac18","ub2629c00192563a550a0c0d49c6a5918"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""กรุณาติดต่อ

http://line.me/ti/p/~405_pom










☆ ─═हई..तุএച้ට௮..ईह═─ ☆
""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Tukimin ",
    "cName2":"Tukiyem ",
    "cName3":"Sarimin ",
    "cName4":"Kucrut ",
    "cName5":"Junaedi ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":True, # Ga Kepake(Yang Gabung langsung di kick :D) Udah  Udah ada Protect Cancell
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        #if op.type == 5:
        #    if wait["autoAdd"] == True:
        #        cl.findAndAddContactsByMid(op.param1)
        #        if (wait["message"] in [""," ","\n",None]):
        #            pass
        #        else:
        #            cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                try:
                  #cl.sendText(op.param1,cl.getContact(op.param2).displayName + "คุณไม่ได้รับสิทธิ์ในการเปิด QR")
                  #cl.kickoutFromGroup(op.param1,[op.param2])
                  X = cl.getGroup(op.param1)
                  X.preventJoinByTicket = True
                  cl.updateGroup(X)
                except:
                  #random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "อย่าวุ่นวายกับ QR")
                  #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(Z)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        #if op.type == 13:
          #if wait["Protectcancl"] == True:
            #group = cl.getGroup(op.param1)
            #gMembMids = [contact.mid for contact in group.invitee]
            #if op.param2 not in Bots:
              #if op.param2 in Bots:
                #pass
              #else:
                #try:
                  #ki.cancelGroupInvitation(op.param1, gMembMids)
                  #ki.kickoutFromGroup(op.param1,[op.param2])
                  #cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "แน๊...!!! แอบดึงคนมาอีกแระ...😒😒😒")
                  #ki.kickoutFromGroup(op.param1,[op.param2])
                #except:
                  #ki.cancelGroupInvitation(op.param1, gMembMids)
                  #ki.sendText(op.param1,ki.getContact(op.param2).displayName + "\n" + "แอบดึงใครมาล่ะท่าน ...🙅🙅🙅")
                  #ki.kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                    
        #------Joined User Kick start------#
      #  if op.type == 17: #awal 17 ubah 13
      #     if wait["Protectjoin"] == True:
      #         if op.param2 not in admin and Bots : # Awalnya admin doang
      #             random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            try:
              cl.kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
              #f=codecs.open('st2__b.json','w','utf-8')
              #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
              #f=codecs.open('st2__b.json','w','utf-8')
              #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
              
        if op.type == 19: #bot Ke Kick
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = ki.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Bmid:
              if op.param2 not in Bots or admin:
                try:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Cmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ks.getGroup(op.param1)
                  ks.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Dmid:
              if op.param2 not in Bots or admin:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in admin:
              if op.param2 not in Bots:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  try:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[admin])
                    wait["blacklist"][op.param2] = True
                  except:
                    try:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                      wait["blacklist"][op.param2] = True
                  
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in admin:  
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Admin menu"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Luffy gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Zorro gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Sanji gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Luffy kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Zorro kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Sanji kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Luffy invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Zorro invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Zorro invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"😝😝.....😛.....😝😝")
                  mc = "||Admin for Bot||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")                
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
    #-----------------=Selesai=------------------
            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                #msg.contentType = 13
                #msg.contentMetadata = {'mid': Amid}
                #ki.sendMessage(msg)

                #msg.contentType = 13
                #msg.contentMetadata = {'mid': Bmid}
                #kk.sendMessage(msg)

                #msg.contentType = 13
                #msg.contentMetadata = {'mid': Cmid}
                #kc.sendMessage(msg)
                
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': Dmid}
                #ks.sendMessage(msg)
                
            elif msg.text in ["Me"]:
              if msg.from_ in admin:   
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
              if msg.from_ in admin:  
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
                    
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Ourl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"😈....URL ON....😈")
                    else:
                        random.choice(KAC).sendText(msg.to,"😈....URL ON....😈")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text in ["Luffy buka qr","Luffy open qr"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Plak")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro buka qr","Zorro open qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji open qr","Sanji buka qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Curl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"😻....URL OFF....😻")
                    else:
                        random.choice(KAC).sendText(msg.to,"😻....URL OFF....😻")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text in ["Luffy close qr","Luffy tutup qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro tutup qr","Zorro close qr"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Plak")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji tutup qr","Sanji close qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Ginfo" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "Mmid" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to, msg.from_)
            elif "Mbot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                #ki.sendText(msg.to,Amid)
                #kk.sendText(msg.to,Bmid)
                #kc.sendText(msg.to,Cmid)
                #ks.sendText(msg.to,Dmid)
            elif "Koplaxs" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,Smid)
            elif "Luffy" == msg.text:
              if msg.from_ in admin:
                ki.sendText(msg.to,mid)
            elif "Zorro" == msg.text:
              if msg.from_ in admin:
                kk.sendText(msg.to,Amid)
            elif "Sanji" == msg.text:
              if msg.from_ in admin:
                kc.sendText(msg.to,Bmid)
            #elif msg.text in ["555","555+","5555","55555","55","555555"]:
                #msg.contentType = 7
                #msg.text = None
                #msg.contentMetadata = {
                                     #"STKID": "10",
                                     #"STKPKGID": "1",
                                     #"STKVER": "100" }
                #ki.sendMessage(msg)
                
            elif msg.text in ["หรา"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                
            elif msg.text in ["พี่","ท้าว"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                
            elif msg.text in ["บอท"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                
            elif msg.text in ["ค่ะ","จ้า","คับ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                
            elif msg.text in ["อะไร"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                
            elif msg.text in ["อืม"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome","มาจ้า","มาใหม่"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                
            elif msg.text in ["TL: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Bot1 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            #elif msg.text in ["Joinn on","joinn on"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == True:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"Done")
                #else:
                    #wait["Protectjoin"] = True
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"done")
            #elif msg.text in ["Joinn off","joinn off"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == False:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
                #else:
                    #wait["Protectjoin"] = False
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set"]:
              if msg.from_ in admin:
                md = "⭐Status Proteksi⭐\n*============*\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+=" Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n*============*\n⭐─═हई..तุএച้ට௮..ईह═─⭐\n*============*"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text in ["แอบ","Ctv","ที่รัก"]:
              #if msg.from_ in admin:
                cl.sendText(msg.to, "...............")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2

            elif msg.text in ["Dctv","อ่าน","อยู่ไหน"]:
                 #if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "     ||ตรวจสอบคนอ่าน||\n=================\n%s\n\n=================\n||─═हई..तุএച้ට௮..ईह═─||\n=================\n%s-=รักนะแอบอ่าน จุฟๆ=-\nตั้งจุดเริ่มต้นตั้งแต่เวลา\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "กรุณาส่ง  [Ctv] เพื่อตั้งจุดเริ่มต้น\nขอได้รับความขอบคุณจากเรา ♪")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Kuy","One piece","Join kuy"]: #Panggil Semua Bot
              if msg.from_ in owner:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                print "Semua Sudah Lengkap"
                        
            elif msg.text in ["Kampret join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Luffy join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Zorro join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Sanji Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["ชิ้ว...","Kabur all","Kaboor all"]: #Bot Ninggalin Group termasuk Bot Induk
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["ชิ้วๆๆ"]: #Semua Bot Ninggalin Group Kecuali Bot Induk
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            elif msg.text in ["Bye zorro"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye sanji"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Ussop"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe1"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe2"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe3"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["tagall","เรียกมา","เรียกคน"]:
              if msg.from_ in admin:
                 group = cl.getGroup(msg.to)
                 group = cl.getGroup(msg.to)
                 k = len(group.members)//100
                 for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
#----------------------------- TAG ALL MEMBER -------------------------------
            if msg.text.lower() in ["@@@@"]:
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                 if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                 if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                 if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                 if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                    cl.sendText(receiver, "Members :"+str(jml))

                    
            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Ready op" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Ready op","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"Eh Kontol Ini Room apaan?")
                    random.choice(KAC).sendText(msg.to,"Ratain aja lah\nRoom Ga Berguna..")
                    random.choice(KAC).sendText(msg.to,"Jangan Baper yah Tollll;")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target in Bots:
                            pass
                          elif target in admin:
                            pass
                          else:
                            try:
                              klist=[cl,ki,kk,kc,ks]
                              kicker=random.choice(klist)
                              kicker.kickoutFromGroup(msg.to,[target])
                              print (msg.to,[g.mid])
                            except:
                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              random.choice(KAC).sendText(msg.to,"Koq Ga Ditangkis Njiiing?\nLemah Banget Nih Room")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"] [0] ["M"]
                for x in key["MENTIONEES"]:
                  targets.append(x["M"])
                for target in targets:
                  try:
                    cl.kickoutFromGroup(msg.to,[target])
                  except:
                    cl.sendText(msg.to,"Error")
        #----------------Fungsi Kick User Target Finish----------------------#
				           
										#----------------Fungsi Kick User Target Finish----------------------# 
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!����")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                bctxt = msg.text.replace("Bc ","")
                a = cl.getGroupIdsJoined()
                a = ki.getGroupIdsJoined()
                a = kk.getGroupIdsJoined()
                a = kc.getGroupIdsJoined()
                a = ks.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
                  ki.sendText(taf, (bctxt))
                  kk.sendText(taf, (bctxt))
                  kc.sendText(taf, (bctxt))
                  ks.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["LG"]: #Melihat List Group
              if msg.from_ in admin:
                gids = cl.getGroupIdsJoined()
                h = ""
                for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                  cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                  h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                  cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Byeall","Botbye"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = ks.getGroupIdsJoined()
                for i in gid:
                  ks.leaveGroup(i)
                  kc.leaveGroup(i)
                  ki.leaveGroup(i)
                  kk.leaveGroup(i)
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sayonara")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
  #------------------------End---------------------

  #-----------------End-----------
            elif msg.text in ["Op katakan hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                

#-----------------------------------------------
            elif msg.text in ["นางฟ้า"]:
                ki.sendText(msg.to,"ใครรู้ตัวว่าสวย มาลงวงด้วยกันสิจร๊")
                
            elif msg.text in ["บ้านคนรวย"]:
                ki.sendText(msg.to,"บ้านดี บ้านรอบอุ่น ท้าวหล่อ สปอร์ต ใจดี  กทม.")
                
            elif msg.text in ["เลขา"]:
                ki.sendText(msg.to,"เลขา ทำงานหน่อย มัวแต่เลี้ยงลูก")
                
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                
            elif msg.text in ["มาลงวงกัน"]:
                ki.sendText(msg.to,"เร่เข้ามา บ้านนี้กลุ่มนี้มีของดีมากมายให้ทุกท่านได้เลือกและจับจอง  ขอบคุณที่ไว้ใจเรา")
                
            elif msg.text in ["เทวดา"]:
                ki.sendText(msg.to,"ลงวงช่วยผมหน่อย คร้าบ ")
                
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Group Kami")
            elif msg.text in ["ลุง","ลุงป้อม","พี่ป้อม","พี่ดนัย","พี่เก่ง","หมอจ้อย"]:
                cl.sendText(msg.to,"พี่เค้าอาบน้ำอยู่ค่ะ มีอะไรฝากข้อความไว้ค่ะ")
                #ki.sendText(msg.to,"ชิ จะเก็บไว้กกคนเดียวก้อบอกสิเธอ")
#-----------------------------------------------
            elif msg.text in ["สวย","สวยจุง","สวยจัง","น่ารัก","น่ารักก","น่ารักจัง"]:
                cl.sendText(msg.to,"เปลี่ยนจากคำชม เป็นค่าเทอมได้มั้ยคร๊")
                
            elif msg.text in ["มาคับ","มาค่ะ","มาครับ","ป่ะ","ไป"]:
                cl.sendText(msg.to,"นู๋ไม่ใช่คนใจง่ายนะ รอแปปเก็บเสื้อผ้าก่อน")
                
            elif msg.text in ["เงีบยจัง","เงียบ"]:
                cl.sendText(msg.to,"ก้อแค่ อยากอยู่เงียบๆด้วยกันสองคน")
                
            elif msg.text in ["ตื่น"]:
                cl.sendText(msg.to,"ไม่อ่ะ นอนกอดผัวต่อดีฟ่า ชิ")
                
            elif msg.text in ["นอน","ฝันดี"]:
                cl.sendText(msg.to,"ต๊ายตายยย  ได้เวลานอนกับผัวแล้วรึนี่ 👌👌")
                
            elif msg.text in ["ว่าง","ว่างค่ะ","ว่างจ้า"]:
                cl.sendText(msg.to,"ป่ะ ตีดัมมี่กัน ยังขาดอีกขา มาๆๆๆๆ")
                
            elif msg.text in ["ห๊ะ","อัยยะ"]:
                cl.sendText(msg.to,"อาห๊ะ โหย่วโหยย.......")
              
            elif msg.text in ["เป็นอะไร","ทำไม","มีอะไรกันรึ","มีไรกัน"]:
                cl.sendText(msg.to,"ผัวทิ้งค่ะ นู๋โดนผัวทิ้ง......😭😭")
                
            elif msg.text in ["บอทตาย","ตายอีกแระ"]:
                cl.sendText(msg.to,"ขอเชิญเจ้าภาพร่วมกรวดน้ำ มาๆๆ จุ่มมือลง")
                
            elif msg.text in ["รับยอดคับ","รับยอดค่ะ"]:
                cl.sendText(msg.to,"ขอกู้สักพันดิ จะไปทำนม 👌👌")
	          
            elif msg.text in ["บอท"]:
                cl.sendText(msg.to,"♠♠♠  รับลงบอท siriv10 ♠♠♠\n\n\nโปรดใช้วิจารณญาณในการสั่งซื้อ\n\nไม่รับดึง ลช\nไม่รับลบห้อง\nไม่รับรันกลุ่ม\n\n\nรับเขียนบอทโต้ตอบ\nรับทำแอพ LINE แบบส่วนตัว\n\n\nโปรดใช้วิจารณญาณในการสั่งซื้อ\n\n\n\nสนใจติดต่อ\nline : 405_pom\nhttp://line.me/ti/p/~405_pom")
                
            elif msg.text in ["กำ"]:
                cl.sendText(msg.to,"อุต๊ะ กำๆดูดๆ ลูบๆคลำๆ ขยำๆๆๆ แล้วก้อทิ้ง􏿿")
                
            elif msg.text in [" tagall","tag all","tagall","Tagall"]:
                ki.sendText(msg.to,"ส่งผิดโว้ย...!!!\n\n\n\nแบร่.............")
                
            elif msg.text in ["ไม่มีตัง","ไม่มีเงิน","ไม่มีเงินค่ะ"]:
                cl.sendText(msg.to,"ยืมท้าวก่อนสิจร๊  ท้าวบ้านนี้เค้าใจดี แถมน่ารักด้วย􏿿")
                
            elif msg.text in ["ปิดวงจ้า","ปิดวงค่ะ","ปิดวง"]:
                cl.sendText(msg.to,"เย้.. นอนล่ะ รอรับตังจากท้าว")
                
            elif msg.text in ["พูดเพราะจังตัวเอง  มีผัวยัง"]:
                ki.sendText(msg.to,"ยังค่ะ แต่กำลังมองหาคนแถวนี้อยู่นะ 😈😈")
                
            elif msg.text in ["เลขา","เลขาไปไหน"]:
                ki.sendText(msg.to,"จะเรียกเลขาทำไม มีนู๋คนเดียวกะปวดหัวแย่แระ")
                
            elif msg.text in ["ไปเที่ยว","ไปเที่ยวไหน","ไปเท่ว","ไปเท่วไหน","ไปเที่ยวที่ไหน"]:
                ki.sendText(msg.to,"แอบไปเท่วไม่ชวนกันบ้างเลยนะตะเอง")
                
            elif msg.text in ["ใช่เลย"]:
                ki.sendText(msg.to,"จิงหรา นู๋ว่าไม่น่าใช่นะ 😀😀")
	          #----------------------------------
	          
	          
                
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Tukang Sayur On")
                #ki.sendText(msg.to,"Tukang Colli On")
                #kk.sendText(msg.to,"Tukang Boker On")
                #kc.sendText(msg.to,"Tukang Becak On")
                #ks.sendText(msg.to,"Tukang Boong")
                cl.sendText(msg.to,"Semua Udah Hadir Boss\nSiap Protect Group\nAman Gak Aman Yang Penting Anu")
      #-------------Fungsi Respon Finish---------------------#
                            

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in admin:
                start = time.time()
                #cl.sendText(msg.to, "Sabar Plak...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Gc","gcreator"]:
              if msg.from_ in owner:
                cl.sendText(msg.to,"แสดงรายชื่อผู้สร้างกลุ่ม")    
                ginfo = cl.getGroup(msg.to)
                gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["555","5555","55555","55555","555+","5555+"]:
                 quote = ['อารมย์ดีแบบนี้มาลงวงกันดีกว่า 😂😂😂.','อุ้ยต๊ายตาย คนน่ารักขำเป็นด้วย..','อย่าขำมาก ไม่มีอารมย์','นิดๆหน่อยๆก้อขำแระ คนเราเนาะ','จะขำอะไรมากมายล่ะคุณเจ๊ ????','อย่าขำสิ นู๋กำลังเศร้า','????????????????????????????\n\n\n\n\n\nขำมากเด่วจับทำเมียซะเลย']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            #-------------
            #elif msg.text in ["นางฟ้า"]:
                 #cl.sendText("ใครรู้ตัวว่าสวย ก้อมาลงจร๊")
                  
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                #wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nยินดีต้อนรับเข้าสู่ ....\nกลุ่ม➡ " + str(ginfo.name))
          print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if op.param2 in Bots:
             return
          cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nโอกาสหน้าเจอกันใหม่นะ ")
          print "MEMBER HAS LEFT THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by ⭐⭐Koplaxs⭐⭐👈\n\n™SMULE VOICE FAMILY™")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"=====Ready=====\n[★]Bot Protect For Group\n[★]\n[★]Selfbot in Your Account[★]\n- 1 Selfbot 1 Bot Assist\n- 1 Selfbot 2 Bot Assist\n- 1 Selfbot 3 Bot Assist\n- 1 Selfbot 4 Bot Assist\n- 1 Selfbot 5 Bot Assist\n\nMau Coba Atau Test Terlebih Dahulu Bisa\nMinat??? PM Id Line @hanavy1992\nLagu Promo Lho Kak\n===[★]One Piece Bot Protect[★]===")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,500):
        hasil = cl.activity(limit=500)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ^One Piece Bot^\nStatus Boss udah Kami Like\nOwner Kami :\nHanavy Koplaxs")
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"=====Ready=====\n[★]Bot Protect For Group\n[★]\n[★]Selfbot in Your Account[★]\n- 1 Selfbot 1 Bot Assist\n- 1 Selfbot 2 Bot Assist\n- 1 Selfbot 3 Bot Assist\n- 1 Selfbot 4 Bot Assist\n- 1 Selfbot 5 Bot Assist\n\nMau Coba Atau Test Terlebih Dahulu Bisa\nMinat??? PM Id Line @hanavy1992\nLagu Promo Lho Kak\n===[★]One Piece Bot Protect[★]===")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
