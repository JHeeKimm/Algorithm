function solution(maps) {
    const n = maps.length
    const m = maps[0].length
    const visited = Array.from({length:n}, ()=>Array(m).fill(false))
    
    const dx = [-1,0,1,0]
    const dy = [0,-1,0,1]
    const q = [[0,0,1]] // [y,x,거리]
    visited[0][0] = true
    
    while (q.length){
        const [y,x,dist] = q.shift()
        
        if(y===n-1 && x===m-1){
            return dist;
        }
        
        for(let i=0; i<4; i++){
            const ny=y+dy[i]
            const nx=x+dx[i]
            
            if(ny>=0 && ny<n && nx>=0 && nx<m && !visited[ny][nx] && maps[ny][nx]===1){
                visited[ny][nx] = true
                q.push([ny,nx,dist+1])
            }
        }
    }
    return -1
}