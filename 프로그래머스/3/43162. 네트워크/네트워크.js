function solution(n, computers) {
    const visited = new Array(n).fill(false)
    let count = 0
    
    function dfs(node) {
        visited[node] = true;

        for (let i = 0; i < n; i++) {
            if (!visited[i] && computers[node][i] === 1) {
                dfs(i); // 연결되어 있고, 아직 방문 안한 컴퓨터로 이동
            }
        }
    }

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);  // 방문하지 않은 컴퓨터에서 DFS 시작
            count++; 
        }
    }
    return count;
}