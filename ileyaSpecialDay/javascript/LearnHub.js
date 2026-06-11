const prompt = require("prompt-sync") ();
console.log("========   LEARN   HUB   ========");
console.log();

let studentsData = [];

let numbersOfStudent = Number(prompt("Enter Numbers Of Student Enrolled: "));
let numbersOfQuiz = Number(prompt("Enter Numbers Of Quiz Taken: "));

for(let students = 1; students < numbersOfStudent + 1; students++) {
    console.log();
    console.log("=====   Student  " + students + " =====");

    let studentsScore = [];
    let totalScore = 0;
    
    for(let quiz = 1; quiz < numbersOfQuiz + 1; quiz++) {
        let scoreForQuiz = Number(prompt("Score For Quiz:" + quiz + ": "));

	studentsScore.push(scoreForQuiz);
	totalScore += scoreForQuiz;
    }
}

    let averageScore = totalScore / numbersOfQuiz;

    let studentRecord = {
        name: `Student ${students + 1}`,
	quizScore: studentsScore,
	average: averageScore
    }

    studentsData.push(studentRecord);

console.log();
console.log("=====    QUIZ GRADE REPORT    =====");
console.log();

let headerDetails = `STUDENT:<15`;

for(let quizIndex : numbersOfQuiz.length) {
    headerDetails += ``
}
