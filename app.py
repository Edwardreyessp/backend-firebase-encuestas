import pyrebase

config = {
  "apiKey": "AIzaSyCiD59Pcm0fZdhZNksigMRTnUEnWtpe78A",
  "authDomain": "encuestas-d19ab.firebaseapp.com",
  "projectId": "encuestas-d19ab",
  "storageBucket": "encuestas-d19ab.appspot.com",
  "messagingSenderId": "259304377291",
  "appId": "1:259304377291:web:16743679fbbc444628444e",
  "measurementId": "G-QF4N3G68HP",
  "databaseURL": "https://encuestas-d19ab-default-rtdb.firebaseio.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Push data
questions = {
  "Q_10_1": {
    "enunciado": "Pensando en los problemas del pa\u00eds, \u00bfcu\u00e1l cree usted que es el problema m\u00e1s importante en estos momentos? ", 
    "respuestas": {
      "1": {
        "color": "#BFBFBF", 
        "respuesta": "Inseguridad "
      }, 
      "10": {
        "color": "#BFBFBF", 
        "respuesta": "Ns/Nc"
      }, 
      "2": {
        "color": "#BFBFBF", 
        "respuesta": "Crisis econ\u00f3mica "
      }, 
      "3": {
        "color": "#BFBFBF", 
        "respuesta": "Narcotr\u00e1fico "
      }, 
      "4": {
        "color": "#BFBFBF", 
        "respuesta": "Mal gobierno/Gobernantes "
      }, 
      "5": {
        "color": "#BFBFBF", 
        "respuesta": "Desempleo "
      }, 
      "6": {
        "color": "#BFBFBF", 
        "respuesta": "Educaci\u00f3n "
      }, 
      "7": {
        "color": "#BFBFBF", 
        "respuesta": "Servicios de salud"
      }, 
      "8": {
        "color": "#BFBFBF", 
        "respuesta": "Contagios de covid-19"
      }, 
      "9": {
        "color": "#BFBFBF", 
        "respuesta": "Otro \u00bfCu\u00e1l? _______________________"
      }
    }
  }, 
  "Q_3_1": {
    "enunciado": "Si hoy fuera la elecci\u00f3n para elegir diputados federales, \u00bfpor cu\u00e1l partido votar\u00eda usted? ", 
    "respuestas": {
      "1": {
        "color": "#00569D", 
        "respuesta": "Partido Acci\u00f3n Nacional (PAN)"
      }, 
      "10": {
        "color": "#C91F39", 
        "respuesta": "Ninguno"
      }, 
      "11": {
        "color": "#ED62A0", 
        "respuesta": "Prefiero no contestar"
      }, 
      "2": {
        "color": "#E20613", 
        "respuesta": "Partido Revolucionario Institucional (PRI)"
      }, 
      "3": {
        "color": "#FFD90F", 
        "respuesta": "Partido de la Revoluci\u00f3n Democr\u00e1tica (PRD)"
      }, 
      "4": {
        "color": "#FF0000", 
        "respuesta": "Partido del Trabajo (PT)"
      }, 
      "5": {
        "color": "#58B04B", 
        "respuesta": "Partido Verde Ecologista de M\u00e9xico (PVEM)"
      }, 
      "6": {
        "color": "#FF4000", 
        "respuesta": "Movimiento Ciudadano (MC)"
      }, 
      "7": {
        "color": "#922514", 
        "respuesta": "Morena"
      }, 
      "8": {
        "color": "#168CA6", 
        "respuesta": "Candidato Independiente"
      }, 
      "9": {
        "color": "#CC2EFA", 
        "respuesta": "Anular\u00eda"
      }
    }
  }
}

db.push(questions)