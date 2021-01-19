from flask import Flask, request 
app = Flask(__name__) 


class Problem():
    def __init__(self, Pnum, Pname, Solved, Pcond, Pdetail, Pinout):
        self.Pnum = Pnum
        self.Pname = Pname
        self.Solved = Solved
        self.Pcond = Pcond
        self.Pdetail = Pdetail
        self.Pinout = Pinout

# deta base 에 있는 정보
p_1001 = Problem("1001", "a+b", "Null", ["0.5초", "128MB"],
["2개의 숫자 a,b 를 입력받아 합을 출력하시오.", "0 < a,b <100", "첫째 줄에 a+b를 출력한다." ], 
[["20 4"], "24"])
p_1002 = Problem("1002", "a-b", "Null", ["0.5초", "128MB"],
["2개의 숫자 a,b를 입력받아 차을 출력하시오.", "0 < a,b <100", "첫째 줄에 a-b를 출력한다." ], 
[["20 4"], "16"])
p_1003 = Problem("1003", "ab", "Null", ["0.5초", "128MB"],
["2개의 숫자 a,b를 입력받아 곱을 출력하시오.", "0 < a,b <100", "첫째 줄에 ab를 출력한다." ], 
[["20 4"], "80"])
p_1004 = Problem("1004", "a/b", "Null", ["0.5초", "128MB"],
["2개의 숫자 a,b 를 입력받아 몫을 출력하시오.", "0 < a,b <100", "첫째 줄에 a/b를 출력한다." ], 
[["20 4"], "5"])
p_1005 = Problem("1005", "a%/b", "Null", ["0.5초", "128MB"],
[",2개의 숫자 a,b를 입력받아 나머지을 출력하시오.", "0 < a,b <100", "첫째 줄에 a%b를 출력한다." ], 
[["20 4"], "0"])

listt = [p_1001,p_1002,p_1003,p_1004,p_1005]


@app.route('/',methods=['POST'])
def hello():
    a = dict(request.get_json())
    return str(a["Pnum"])


@app.route('/p_info/', methods=['POST'])
def P_info():
    
    problem_number = request.get_json()["Pnum"] #1001
    return {
	"Pnum" : listt[problem_number-1001].Pnum,
	"Pname" : listt[problem_number-1001].Pname,
	"Solved": listt[problem_number-1001].Solved,
	"Pcond" : listt[problem_number-1001].Pcond,
	"Pdetail" : listt[problem_number-1001].Pdetail,
	"Pinout" : listt[problem_number-1001].Pinout
}



@app.route('/result', methods=['POST'])
def result():
    pnum = dict(request.get_json())["Pnum"]
    res = dict(request.get_json())["Result"]
    listt[pnum-1001].Solved = res

    return listt[pnum-1001].Solved



if __name__ == '__main__': 
    app.run(debug=True) #코드 수정하면 바로바로 서버 restart 해줌

# {
#   "Pnum": 1005
# }

# {
# 	"Pnum" : 1001,
# 	"Result" : "T"
# }