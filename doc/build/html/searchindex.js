Search.setIndex({docnames:["actions","actions.api","actions.constants","actions.db_connection","actions.model","actions.services","actions.utils","index","modules"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":2,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.todo":2,sphinx:56},filenames:["actions.rst","actions.api.rst","actions.constants.rst","actions.db_connection.rst","actions.model.rst","actions.services.rst","actions.utils.rst","index.rst","modules.rst"],objects:{"":{actions:[0,0,0,"-"]},"actions.api":{Car_API:[1,0,0,"-"],Record_API:[1,0,0,"-"],Report_API:[1,0,0,"-"],User_API:[1,0,0,"-"]},"actions.api.Car_API":{Car_API:[1,1,1,""]},"actions.api.Car_API.Car_API":{addCar:[1,2,1,""],getBodyTypes:[1,2,1,""],getCarsWithparams:[1,2,1,""],getColors:[1,2,1,""],getMakes:[1,2,1,""],getSeatNumbers:[1,2,1,""],getWholeCars:[1,2,1,""],pushtest:[1,2,1,""],removeCar:[1,2,1,""],reportCar:[1,2,1,""],updateCar:[1,2,1,""]},"actions.api.Record_API":{Record_API:[1,1,1,""]},"actions.api.Record_API.Record_API":{book:[1,2,1,""],cancel_booking:[1,2,1,""],checkRecord:[1,2,1,""],getRecords:[1,2,1,""]},"actions.api.Report_API":{Report_API:[1,1,1,""]},"actions.api.Report_API.Report_API":{closeReport:[1,2,1,""],getReports:[1,2,1,""]},"actions.api.User_API":{User_API:[1,1,1,""]},"actions.api.User_API.User_API":{checkUserName:[1,2,1,""],deleteUser:[1,2,1,""],getUsersWithparams:[1,2,1,""],login:[1,2,1,""],register:[1,2,1,""],updatePassword:[1,2,1,""],updateUser:[1,2,1,""]},"actions.constants":{Sys_Constants:[2,0,0,"-"]},"actions.db_connection":{DBConnection:[3,0,0,"-"]},"actions.db_connection.DBConnection":{DBConnection:[3,1,1,""]},"actions.db_connection.DBConnection.DBConnection":{db:[3,3,1,""],ma:[3,3,1,""]},"actions.model":{Car:[4,0,0,"-"],Car_Make:[4,0,0,"-"],Record:[4,0,0,"-"],Report:[4,0,0,"-"],Role:[4,0,0,"-"],User:[4,0,0,"-"]},"actions.model.Car":{Car:[4,1,1,""],CarModel:[4,1,1,""],CarSchema:[4,1,1,""]},"actions.model.Car.Car":{body_type:[4,3,1,""],car_id:[4,3,1,""],car_location:[4,3,1,""],car_status:[4,3,1,""],color:[4,3,1,""],cost:[4,3,1,""],make:[4,3,1,""],seat_number:[4,3,1,""]},"actions.model.Car.CarModel":{add:[4,2,1,""],find_by_car_id:[4,2,1,""],getBodyTypes:[4,2,1,""],getCars:[4,2,1,""],getCarsWithMake:[4,2,1,""],getCarsWithparams:[4,2,1,""],getColors:[4,2,1,""],getSeatNumbers:[4,2,1,""],removeCar:[4,2,1,""],updateCar:[4,2,1,""],update_status:[4,2,1,""]},"actions.model.Car.CarSchema":{Meta:[4,1,1,""],opts:[4,3,1,""]},"actions.model.Car.CarSchema.Meta":{fields:[4,3,1,""]},"actions.model.Car_Make":{CarMakeModel:[4,1,1,""],CarMakeSchema:[4,1,1,""],Car_Make:[4,1,1,""]},"actions.model.Car_Make.CarMakeModel":{getCarMakes:[4,2,1,""]},"actions.model.Car_Make.CarMakeSchema":{Meta:[4,1,1,""],opts:[4,3,1,""]},"actions.model.Car_Make.CarMakeSchema.Meta":{fields:[4,3,1,""]},"actions.model.Car_Make.Car_Make":{id:[4,3,1,""],name:[4,3,1,""]},"actions.model.Record":{Record:[4,1,1,""],RecordModel:[4,1,1,""],RecordSchema:[4,1,1,""]},"actions.model.Record.Record":{car_id:[4,3,1,""],est_rent_date:[4,3,1,""],est_return_date:[4,3,1,""],is_cancel:[4,3,1,""],is_return:[4,3,1,""],record_id:[4,3,1,""],user_id:[4,3,1,""]},"actions.model.Record.RecordModel":{add:[4,2,1,""],find_all:[4,2,1,""],find_by_car_id_and_user_id_and_return_and_cancel:[4,2,1,""],find_history_by_user_id:[4,2,1,""],find_newest:[4,2,1,""],find_records_by_user_id_with_all_return:[4,2,1,""],update_is_cancel:[4,2,1,""],update_is_return:[4,2,1,""]},"actions.model.Record.RecordSchema":{Meta:[4,1,1,""],opts:[4,3,1,""]},"actions.model.Record.RecordSchema.Meta":{fields:[4,3,1,""]},"actions.model.Report":{Report:[4,1,1,""],ReportModel:[4,1,1,""],ReportSchema:[4,1,1,""]},"actions.model.Report.Report":{admin_id:[4,3,1,""],car_id:[4,3,1,""],close_date:[4,3,1,""],engineer_id:[4,3,1,""],issue:[4,3,1,""],report_date:[4,3,1,""],report_id:[4,3,1,""]},"actions.model.Report.ReportModel":{add:[4,2,1,""],find_all_reports:[4,2,1,""],getLastReport:[4,2,1,""],update:[4,2,1,""]},"actions.model.Report.ReportSchema":{Meta:[4,1,1,""],opts:[4,3,1,""]},"actions.model.Report.ReportSchema.Meta":{fields:[4,3,1,""]},"actions.model.Role":{Role:[4,1,1,""],RoleSchema:[4,1,1,""]},"actions.model.Role.Role":{role_id:[4,3,1,""],role_name:[4,3,1,""]},"actions.model.Role.RoleSchema":{Meta:[4,1,1,""],opts:[4,3,1,""]},"actions.model.Role.RoleSchema.Meta":{fields:[4,3,1,""]},"actions.model.User":{User:[4,1,1,""],UserModel:[4,1,1,""],UserSchema:[4,1,1,""]},"actions.model.User.User":{email:[4,3,1,""],first_name:[4,3,1,""],last_name:[4,3,1,""],password:[4,3,1,""],role:[4,3,1,""],user_id:[4,3,1,""],username:[4,3,1,""]},"actions.model.User.UserModel":{add:[4,2,1,""],checkUserName:[4,2,1,""],deleteUser:[4,2,1,""],getLastUserId:[4,2,1,""],getUser:[4,2,1,""],getUsersWithparams:[4,2,1,""],login:[4,2,1,""],update:[4,2,1,""],updatePassword:[4,2,1,""]},"actions.model.User.UserSchema":{Meta:[4,1,1,""],opts:[4,3,1,""]},"actions.model.User.UserSchema.Meta":{fields:[4,3,1,""]},"actions.services":{Car_Service:[5,0,0,"-"],Record_Service:[5,0,0,"-"],Report_Service:[5,0,0,"-"],User_Service:[5,0,0,"-"]},"actions.services.Car_Service":{Car_Service:[5,1,1,""]},"actions.services.Car_Service.Car_Service":{addCar:[5,2,1,""],find_by_car_id:[5,2,1,""],getBodyTypes:[5,2,1,""],getCarsWithMake:[5,2,1,""],getCarsWithparams:[5,2,1,""],getColors:[5,2,1,""],getMakes:[5,2,1,""],getSeatNumbers:[5,2,1,""],removeCar:[5,2,1,""],rent:[5,2,1,""],reportCar:[5,2,1,""],return_car:[5,2,1,""],send_pushbullet_with_report_info:[5,2,1,""],updateCar:[5,2,1,""]},"actions.services.Record_Service":{Record_Service:[5,1,1,""]},"actions.services.Record_Service.Record_Service":{book:[5,2,1,""],cancel_booking:[5,2,1,""],find_all:[5,2,1,""],find_by_car_id_and_user_id:[5,2,1,""],find_by_car_id_and_user_id_and_return_and_cancel:[5,2,1,""],find_history_by_user_id:[5,2,1,""],find_records_by_user_id_with_all_return:[5,2,1,""]},"actions.services.Report_Service":{Report_Service:[5,1,1,""]},"actions.services.Report_Service.Report_Service":{add:[5,2,1,""],find_the_new_one:[5,2,1,""],getReports:[5,2,1,""],update:[5,2,1,""]},"actions.services.User_Service":{User_Service:[5,1,1,""]},"actions.services.User_Service.User_Service":{checkUserName:[5,2,1,""],deleteUser:[5,2,1,""],getUsersWithparams:[5,2,1,""],login:[5,2,1,""],register:[5,2,1,""],updatePassword:[5,2,1,""],updateUser:[5,2,1,""]},"actions.utils":{Pushbullet_utils:[6,0,0,"-"],google_calendar_utils:[6,0,0,"-"],parse_qs_plus:[6,0,0,"-"],socket_handler:[6,0,0,"-"]},"actions.utils.Pushbullet_utils":{Pushbullet_utils:[6,1,1,""]},"actions.utils.Pushbullet_utils.Pushbullet_utils":{send_notification_via_pushbullet:[6,2,1,""]},"actions.utils.google_calendar_utils":{Google_Calendar_Utils:[6,1,1,""]},"actions.utils.google_calendar_utils.Google_Calendar_Utils":{"delete":[6,2,1,""],insert:[6,2,1,""]},"actions.utils.parse_qs_plus":{ParserUtils:[6,1,1,""]},"actions.utils.parse_qs_plus.ParserUtils":{parse_qs_plus:[6,2,1,""]},"actions.utils.socket_handler":{Socket_Handler:[6,1,1,""]},"actions.utils.socket_handler.Socket_Handler":{action_decider:[6,2,1,""]},actions:{api:[1,0,0,"-"],constants:[2,0,0,"-"],db_connection:[3,0,0,"-"],model:[4,0,0,"-"],services:[5,0,0,"-"],utils:[6,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute"},terms:{"boolean":5,"class":[1,3,4,5,6],"function":1,"int":[5,6],"new":[1,5,6],"return":[1,4,5,6],"static":6,"true":[1,5],The:6,_dict:6,a_password:5,a_usernam:5,action:[7,8],action_decid:6,add:[1,4,5,6],addcar:[1,5],added:5,admin_id:[4,5],all:[1,4,5],also:5,api:[0,4,5,6,8],applic:2,authent:5,avail:5,base:[1,3,4,5,6],bodi:[1,4,5,6],body_typ:4,book:[1,4,5],book_info:5,calendar:6,can:[1,6],cancel:[1,5],cancel_book:[1,5],car:[0,1,5,6,8],car_api:[0,8],car_id:[4,5],car_loc:[4,6],car_mak:[0,8],car_servic:[0,8],car_statu:4,carmak:4,carmakemodel:4,carmakeschema:4,carmodel:4,carschema:4,chang:5,check:[1,4,5],checkrecord:1,checkusernam:[1,4,5],client:[5,6],close:[1,5],close_d:4,closereport:1,code:6,color:[1,4,5],condit:[1,4],connect:[3,4,6],constant:[0,8],contain:[2,5],content:[7,8],cost:4,creat:3,current:[4,5],data:[4,5,6],databas:[3,4,5],date:[5,6],db_connect:[0,8],dbconnect:[0,8],declar:4,delet:[1,4,6],deleteus:[1,4,5],descript:6,detail:[1,5],dictionari:[5,6],differ:5,each:5,email:[4,5,6],encrypt:5,endpoint:[1,6],engin:[3,5],engineer_id:[4,5],entri:[1,6],est_rent_d:[4,6],est_return_d:[4,6],estim:6,event:6,evnent:6,exist:5,ext:4,factor:5,fals:[1,5],field:4,find:[4,5],find_al:[4,5],find_all_report:4,find_by_car_id:[4,5],find_by_car_id_and_user_id:5,find_by_car_id_and_user_id_and_return_and_cancel:[4,5],find_history_by_user_id:[4,5],find_newest:4,find_records_by_user_id_with_all_return:[4,5],find_the_new_on:5,first:5,first_nam:[4,5],flag:[4,5],flask_marshmallow:[3,4],from:[4,5,6],get:[1,5],getbodytyp:[1,4,5],getcar:4,getcarmak:4,getcarswithmak:[4,5],getcarswithparam:[1,4,5],getcolor:[1,4,5],getlastreport:4,getlastuserid:4,getmak:[1,5],getrecord:1,getreport:[1,5],getseatnumb:[1,4,5],getus:4,getuserswithparam:[1,4,5],getwholecar:1,going:5,googl:6,google_calendar_util:[0,8],has:[1,4,5],histori:5,index:7,indic:[1,4],inform:[1,4,5],input:6,insert:6,is_cancel:[4,5],is_return:[4,5],issu:[4,5],json:5,kwarg:4,last:5,last_nam:[4,5],lateset:5,latest:4,layer:5,list:[1,4,5],locat:6,logic:5,login:[1,4,5],make:[4,5],manufactur:[1,4,5],marshmallow:[3,4],match:5,meta:4,method:5,model:[0,8],modul:[7,8],name:[4,5],need:5,new_password:[4,5],none:3,notif:[5,6],number:[1,4,5],object:[1,3,4,5,6],old_password:5,oper:[1,6],opt:4,order:6,organis:1,otherwis:[1,5],packag:[7,8],page:[5,7],param:[4,5,6],paramet:5,parse_qs_plu:[0,8],parser:6,parserutil:6,password:[1,4,5],point:[1,6],pushbullet:[5,6],pushbullet_util:[0,8],pushtest:1,queri:[4,5],record:[0,1,5,6,8],record_api:[0,8],record_id:[4,6],record_servic:[0,8],recordmodel:4,recordschema:4,regist:[1,5],relat:1,remov:[1,4,5],removecar:[1,4,5],rent:[1,4,5,6],report:[0,1,5,8],report_api:[0,8],report_d:4,report_id:[4,5],report_servic:[0,8],reportcar:[1,5],reportmodel:4,reportschema:4,repres:5,result:[1,5,6],resultproxi:6,return_car:5,role:[0,5,8],role_id:4,role_nam:4,roleschema:4,schema:4,schemaopt:4,search:7,seat:[1,4,5],seat_numb:4,send:[5,6],send_notification_via_pushbullet:6,send_pushbullet_with_report_info:5,sent:[5,6],servic:[0,8],socket:6,socket_handl:[0,8],some:2,sqlalchemi:[3,4],src:7,statu:[4,5],store:4,str:6,string:[5,6],submodul:[0,8],subpackag:8,success:1,successfulli:1,sys_const:[0,8],tabl:[4,5],taken:1,text:6,them:5,titl:6,transform:6,type:[1,4,5],updat:[1,4,5],update_is_cancel:4,update_is_return:4,update_statu:4,updatecar:[1,4,5],updatepassword:[1,4,5],updateus:[1,5],use:[1,5,6],used:[2,4,5,6],user:[0,1,5,8],user_api:[0,8],user_id:[4,5],user_servic:[0,8],usermodel:4,usernam:[1,4,5],userschema:4,util:[0,8],valid:5,via:[5,6],want:6,web:5,whether:[1,4,5],which:[1,4,5],who:5,you:6},titles:["actions package","actions.api package","actions.constants package","actions.db_connection package","actions.model package","actions.services package","actions.utils package","Welcome to Panda_Rental_APIs\u2019s documentation!","src"],titleterms:{action:[0,1,2,3,4,5,6],api:1,car:4,car_api:1,car_mak:4,car_servic:5,constant:2,content:[0,1,2,3,4,5,6],db_connect:3,dbconnect:3,document:7,google_calendar_util:6,indic:7,model:4,modul:[0,1,2,3,4,5,6],packag:[0,1,2,3,4,5,6],panda_rental_api:7,parse_qs_plu:6,pushbullet_util:6,record:4,record_api:1,record_servic:5,report:4,report_api:1,report_servic:5,role:4,servic:5,socket_handl:6,src:8,submodul:[1,2,3,4,5,6],subpackag:0,sys_const:2,tabl:7,user:4,user_api:1,user_servic:5,util:6,welcom:7}})