from flask import Flask
import os

app = Flask(__name__)


#version_from_file = 'none'
#print("[ricc] Starting the super-duper vanilla server in python to say HelloWorld!\n")

def version_from_file():
  with open("VERSION", "r") as f:
    return "".join(f.readlines()).rstrip()

def cloud_deploy_target_short_common():
  return os.environ.get('CLOUD_DEPLOY_TARGET_SHORT_COMMON', '_dunno_')

@app.route('/')
def index():

  version = version_from_file() # "1.1a"
  fav_color = os.environ.get('FAVORITE_COLOR', '#181818') # ~black
  env_app_name = os.environ.get('APP_NAME')
  cd_stage =  os.environ.get('CLOUD_DEPLOY_TARGET')
  ric_msg = os.environ.get('RICCARDO_MESSAGE')
  # moving vars to COMMON from /components/
  fav_color_common = os.environ.get('FAVORITE_COLOR_COMMON', '#282828')
  cloud_deploy_target_common = os.environ.get('CLOUD_DEPLOY_TARGET_COMMON', 'CDTC non datur')
  #cloud_deploy_target_short_common =

  print("[ricc][web.py] INDEX: the super-duper vanilla server in python to say HelloWorld - v{}!\n".format(version))
  return """<h1>App01 (🐍) v<b>{ver}</b></h1>

        Hello world from Skaffold in python! This is a demonstrative app to demonstrate CI/CD with Cloud Deploy and Cloud Build<br/>

        I read version from file and this ./VERSION file is actually read by the build pipeline
        into the Cloud Deploy release name - wOOOt!<br/><br/>

        FAVORITE_COLOR={fav_color}<br/>
        CD_TARGET={cd_stage} <br/>
        CLOUD_DEPLOY_TARGET_COMMON={cloud_deploy_target_common} <br/>
        CLOUD_DEPLOY_TARGET_SHORT_COMMON={cloud_deploy_target_short_common} <br/>
        <br/>
        APP_NAME={env_app_name} <br/>
        RICCARDO_MESSAGE={ric_msg}<br/>
        <br/>

        Favorite Color COMMON from v1.35: <b style='background-color:{fav_color_common};' >{fav_color_common}</b><br/>
        Favorite Color from v1.4: <b style='background-color:{fav_color};' >{fav_color}</b><br/>

        Link to <a href="/statusz" >Statusz</a>.
        <hr/>
          <center>
           <!-- /statusz --> app01 (🐍) v<b>{ver}</b> target: <b>{cloud_deploy_target_short_common}</b>
          </center>
  """.format(
    ver=version,
    fav_color=fav_color,
    fav_color_common=fav_color_common,
    env_app_name=env_app_name,
    cd_stage=cd_stage,
    cloud_deploy_target_common=cloud_deploy_target_common,
    ric_msg=ric_msg,
    cloud_deploy_target_short_common=cloud_deploy_target_short_common())

@app.route('/statusz')
def statusz_page():
    return """app=app01 version={version} target={cloud_deploy_target_common} emoji=🐍\n""".format(
      version=  version_from_file() ,
      cloud_deploy_target_common=cloud_deploy_target_short_common(),
    )
