from lowusage import app
from lowusage.form  import SurvForm
from lowusage.models import db,HOST,EMAIL,ANSWER 

from flask import (
     Flask,
     render_template,
     request,
     make_response,
     url_for,
     redirect,
     flash
)

@app.route('/lowusage/<int:e_id>', methods=['GET','POST'])
def index(e_id):

  page = request.args.get('page', 1, type=int)
  email_qr = EMAIL.query.filter(EMAIL.ID==(e_id)).first()
  email_id = email_qr.ID
  email = email_qr.ML
  #pagination = HOST.query.filter(HOST.Ml==(email_id)).paginate(page=page,per_page=5,error_out=False)
  #pagination = HOST.query(HOST.Hostname,HOST.Ml).outerjoin(ANSWER, HOST.Hostname==ANSWER.Hostname).filter(EMAIL.ID==(e_id))
  pagination = db.session.query(HOST.Hostname, HOST.Ml,HOST.Server_Group,HOST.Emp_name)\
               .outerjoin(ANSWER, HOST.Hostname==ANSWER.Hostname)\
	       .filter(EMAIL.ID==(email_id)).paginate(page=page,per_page=5,error_out=False)

  print(pagination.items)

  
  for item in pagination.items:
      print(item)	      
     
 
  form = SurvForm()
  form_default = SurvForm({})
  p_hostname = request.form.get('phostname' , '')
  if form.validate_on_submit():
      print(request.form)
      p_hostname = request.form.get('phostname')
      p_ans1 = request.form.get('ans1')
      p_ans2 = request.form.get('ans2')
      s_id = request.headers.get('SSO_USER')
      s_name = request.headers.get('EMPNM').encode('iso-8859-1').decode('utf-8')
      s_dep = request.headers.get('DEPTNM').encode('iso-8859-1').decode('utf-8')


      ans = ANSWER(Hostname=p_hostname,Ans1=p_ans1,Ans2=p_ans2,Emp_name=s_name,Emp_dep=s_dep,Emp_id=s_id )
      print(ans)
      #db.session.add(ans)
      db.session.merge(ans)
      db.session.commit()
      s_user = request.headers.get('SSO_USER')
      s_name = request.headers.get('EMPNM').encode('iso-8859-1').decode('utf-8')
      s_department = request.headers.get('DEPTNM').encode('iso-8859-1').decode('utf-8')
      print(s_name)
      flash('data submited!')
      return redirect('/lowusage/{}'.format(e_id))
      

  else:
      #print(request.form)	  
      print('not submited on validate!')
  return render_template('index.html', 
			  email=email,
			  form=form,
			  form_default=form_default,
			  phostname=p_hostname,
			  pagination=pagination,
			  e_id=e_id,
			  )
                                     


@app.route('/', methods=['GET'])
def dashboard():

  page = request.args.get('page', 1, type=int)
  pagination = ANSWER.query.paginate(page=page,per_page=10,error_out=False)
      	  
  return render_template('dashboard.html', pagination=pagination)



