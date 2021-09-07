function solution(priorities, location) {
    let answer = 0;
    while (priorities.length > 0) {
        let first = priorities.shift()
        if (priorities.some(x => x > first)){
            priorities.push(first)
        } else {
            count++;
            if (location == 0) {
                return answer;
            }
        }
        location --
        if (location === -1) {
            location = priorities.length - 1
        }

    }
    return answer;
}