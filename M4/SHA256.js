function hex2bin(hex){
    hex = hex.replace("0x", "").toLowerCase();
    var out = "";
    for(var c of hex) {
        switch(c) {
            case '0': out += "0000"; break;
            case '1': out += "0001"; break;
            case '2': out += "0010"; break;
            case '3': out += "0011"; break;
            case '4': out += "0100"; break;
            case '5': out += "0101"; break;
            case '6': out += "0110"; break;
            case '7': out += "0111"; break;
            case '8': out += "1000"; break;
            case '9': out += "1001"; break;
            case 'a': out += "1010"; break;
            case 'b': out += "1011"; break;
            case 'c': out += "1100"; break;
            case 'd': out += "1101"; break;
            case 'e': out += "1110"; break;
            case 'f': out += "1111"; break;
            default: return "";
        }
    }

    return out;
}

function bin2hexMoodle(bin) {
  let bin2hexMoodle = parseInt(bin, 2).toString(16).toLowerCase();
  if(bin2hexMoodle.length < 8) {
    bin2hexMoodle = SHR(8-bin2hexMoodle.length,bin2hexMoodle);
  }
  return '0x' + bin2hexMoodle;
}


function XOR(text1, text2) {
  let s = '';
  for (i=0; i < text1.length; i++) {
    s += text1[i] ^ text2[i];
  }
  
  return s;
}

function AND(text1, text2) {
  let s = '';
  for (i=0; i < text1.length; i++) {
    s += text1[i] & text2[i];
  }
  
  return s;
}


function NOT(text1) {
  let s = '';
  for (i=0; i < text1.length; i++) {
    s += text1[i] == '1' ? '0' : '1';
  }
  
  return s;
}

function ROTR(int,text) {
  const num = 32 - int;
  var a = text.substring(num)
  return (a.concat(text)).substring(0,32)
}

function SHR(int, text) {
  let s = '';
  
  for (i=0; i < int; i++) {
    s += '0';
  }
  
   return (s.concat(text)).substring(0,32)
}

function σ_0 (m) {
  let rotr7 = ROTR(7,m)
  let rotr18 = ROTR(18,m)
  let shr3 = SHR(3, m)
  let σ0 = XOR(XOR(rotr7,rotr18),shr3);
  return σ0;
}


function σ_1 (m) {
  let rotr17 = ROTR(17, m);
  let rotr19 = ROTR(19, m);
  let shr10 = SHR(10, m);
  let σ1 = XOR(XOR(rotr17,rotr19),shr10);
  return σ1;
}


function Σ_0 (m) {
  let rotr2 = ROTR(2,m)
  let rotr13 = ROTR(13,m)
  let rotr22 = ROTR(22,m)
  let Σ0 = XOR(XOR(rotr2,rotr13),rotr22);
  return Σ0;
}

function Σ_1 (m) {
  let rotr6 = ROTR(6,m)
  let rotr11 = ROTR(11,m)
  let rotr25 = ROTR(25,m)
  let Σ1 = XOR(XOR(rotr6,rotr11),rotr25);
  return Σ1;
}

function σ_0_from_hexa(hexa) {
  let m = hex2bin(hexa);  
  let  σ0 = σ_0(m);
  
  return bin2hexMoodle(σ0);
}

function σ_1_from_hexa(hexa) {
  let m = hex2bin(hexa);  
  let  σ1 = σ_1(m);

  return bin2hexMoodle(σ1);
}

function Σ_0_from_hexa(hexa) {
  let m = hex2bin(hexa);  
  let  Σ0 = Σ_0(m);
  
  return bin2hexMoodle(Σ0);
}

function Σ_1_from_hexa(hexa) {
  let m = hex2bin(hexa);  
  let  Σ1 = Σ_1(m);
  
  return bin2hexMoodle(Σ1);
}

function Maj(a,b,c) {  
  const a_b = AND(a,b);
  const a_c = AND(a,c);
  const b_c = AND(b,c);
  
  return XOR(XOR(a_b,a_c),b_c);
}

function Maj_from_hexa(a,b,c) {
  a = hex2bin(a.substring(2));  
  b = hex2bin(b.substring(2));  
  c = hex2bin(c.substring(2));  
  
  let maj = Maj(a,b,c);
  
  return bin2hexMoodle(maj);
}

function Ch(e,f,g) {  
  const e_f = AND(e,f);   
  const e_g = AND(NOT(e), g);
  
  return XOR(e_f,e_g);
}

function Ch_from_hexa(e,f,g) {
  e = hex2bin(e.substring(2));  
  f = hex2bin(f.substring(2));  
  g = hex2bin(g.substring(2));  
  
  let ch = Ch(e,f,g);
  
  return bin2hexMoodle(ch);
}

/* EJERCICIS PER PRACTICAR */

/*
Calculeu el resultat de la funció σ0(a), utilitzada en el SHA256, sobre el valor a=0xf0fff000.
Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/

console.log('σ_0_from_hexa');
σ_0_from_hexa('f0fff000'); // 0xe3fe3ddf

/*
Calculeu el resultat de la funció σ0(a), utilitzada en el SHA256, sobre el valor a=0xff00f00f.

Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/

σ_0_from_hexa('ff00f00f'); //0x3c1de021


/*
Calculeu el resultat de la funció σ1(a), utilitzada en el SHA256, sobre el valor a=0xfff0f00f.
Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/
console.log('σ_1_from_hexa');

σ_1_from_hexa('fff0f00f'); // 0x6639fc3a
/*
Calculeu el resultat de la funció σ1(a), utilitzada en el SHA256, sobre el valor a=0xfff0f0f0.
Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/
σ_1_from_hexa('fff0f0f0'); // 0x66599c3a

/*
Calculeu el resultat de la funció σ1(a), utilitzada en el SHA256, sobre el valor a=0xf0f0000f.

Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/
σ_1_from_hexa('fff0f00f'); 
σ_1_from_hexa('f0f0000f');


/*
Calculeu el resultat de la funció Σ0(a), utilitzada en el SHA256, sobre el valor a=0xf000f0ff.
Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/

console.log('Σ0: ');
Σ_0_from_hexa('f000f0ff'); // 0x783c43f8
Σ_0_from_hexa('f00f0000'); // 0x000443b8

/*
Calculeu el resultat de la funció Σ1(a), utilitzada en el SHA256, sobre el valor a=0xffff0f0f.
Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/
/*
Calculeu el resultat de la funció Σ1(a), utilitzada en el SHA256, sobre el valor a=0xff0ff0ff.
Expreseu el resultat en hexadecimal en el mateix format que es mostra el valor d'entrada.
*/


console.log('Σ_1: ');
Σ_1_from_hexa('ff0ff0ff'); // 0x21878422
Σ_1_from_hexa('ff00ff0f'); // 0x5e7c641c



/*
Calculeu el resultat de la funció Maj(a,b,c), utilitzada en el SHA256, sobre els valors a=0xfff0ffff, b=0xff0fff0f, c=0xf0f0f0f0.
Expreseu el resultat en hexadecimal en el mateix format que es mostren els valors d'entrada.
*/


console.log('Maj_from_hexa: ');

let a = '0x6a09e667'
let b = '0xbb67ae85'
let c = '0x3c6ef372'

Maj_from_hexa(a,b,c);

a='0xfff0ffff', b='0xff0fff0f', c='0xf0f0f0f0';

Maj_from_hexa(a,b,c);

a='0xffff0f0f', b='0xf0ffffff', c='0xf0fffff0';
Maj_from_hexa(a,b,c); //0xf0ffffff  


/*
Calculeu el resultat de la funció Ch(a,b,c), utilitzada en el SHA256, sobre els valors a=0xff000fff, b=0xf00f0ff0, c=0xff0f00ff.
Expreseu el resultat en hexadecimal en el mateix format que es mostren els valors d'entrada.
*/

console.log('Ch_from_hexa: ');

let e = '0x510e527f';
let f = '0x9b05688c';
let g = '0x1f83d9ab';

Ch_from_hexa(e,f,g); // 0x1f85c98c.

e='0xff000fff', f='0xf00f0ff0', g='0xff0f00ff';
Ch_from_hexa(e,f,g); // 0xf00f0ff0.

e='0xf0000000', f='0xfff0f0ff', g='0xf0ff00ff';
Ch_from_hexa(e,f,g); // 0xf00f0ff0.

