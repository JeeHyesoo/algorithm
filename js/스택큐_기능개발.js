function solution(progresses, speeds) {
    let answer = [];
    progresses = progresses.map((item, index)=>{
        return Math.ceil((100 - item) / speeds[index])
    });
    let count = 0;
    let reference = progresses[0];
    console.log(progresses);
    for(let i = 0; i < progresses.length; i++){
        if (progresses[i] <= reference){
            count++;
            console.log(count);
        }else{
            reference = progresses[i];
            answer.push(count);
            count = 1;
        }
        
    }
    answer.push(count);
    return answer;
}