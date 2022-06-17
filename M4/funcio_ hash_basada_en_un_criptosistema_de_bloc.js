/*
bit: 4 bit d'entrada
*/
function g(bit) {
  const a = XOR(bit[0],bit[1])
  const b = XOR(bit[2],bit[3])
  
  return a.toString() + b.toString();
}

const XOR = (bit1, bit2)=>{
  return (bit1 ^ bit2).toString();
}

function XOR_CHAR(text1, text2) {
  let s = '';
  for (i=0; i < text1.length; i++) {
    s += text1[i] ^ text2[i];
  }
  
  return s;
}

function h(hash, VI) {
  let m1 = hash.substring(0,4);
  let m2 = hash.substring(4);
  const k = g(VI);
  
  const c = XOR(m1[0], k[0]) + XOR(m1[1], k[1]) + XOR(m1[2], k[1]) + XOR(m1[3], k[0]);
  const h1 = XOR_CHAR(c,VI);
 

  const k2 = g(h1);
  const c2 = XOR(m2[0], k2[0]) + XOR(m2[1], k2[1]) + XOR(m2[2], k2[1]) + XOR(m2[3], k2[0]);
  const h2 = XOR_CHAR(c2,h1);
  
  return h2;
  
}

let hash = '11001110';
let VI= '0111';
h(hash, VI);

hash = '00111100';
VI = '0010';
h(hash, VI);
