const prompt = require("prompt-sync") ();

let score_storage = [];

let teams = Number(prompt("Enter Number OF Team: "));
let matches = Number(prompt("Enter Numbers Of Matches Played: "));

for(let team = 0; team < teams; team++) {
   console.log(`---  TEAM  ${team + 1}  ---`);

   for(let match = 0; match < matches; match++) {
      let match_input = Number(prompt(`Score In Match ${match + 1}: `));

      score_storage.push(match_input);
      }
     
   }
   for(let scores of score_storage) {
   console.log("Scores:",scores[score_storage]);
   console.log();
   }

let counter = 1;
let sum = 0;

console.log("========   TOURNAMENT   SCOREBOARD   ========");

for(let things in score_storage) {
	console.log(things[score_storage]);
}
