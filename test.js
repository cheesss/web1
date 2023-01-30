const user1 = {
    age: 11,
    name :'1'
};

const user1Copy = Object.assign({}, user1);
//user1 정보를 {}로 초기화된 user1Copy에 대입해준다.

console.log(user1Copy)

function isLynGenius(a){
    if(a.includes("천재" )){
        console.log(a.includes("천재"));
        console.log("틀린말이 있습니다.");
    } else{
        console.log(a.includes("천재"));
        console.log("통과");
    }
}

isLynGenius("채린이는 천재다");