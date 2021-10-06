function my_name(code,word){
    let arr=['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']
    if(code=="tr"|| code == "az"){
        temp=word;
        temp = temp.replace('\u0049', '\u0131');
        return temp;
    }
    else if(code =="ga" || code=="ga-IE"){
      temp="";
      if (word[0] == 't' || word[0] == 'n'){
          for(i=0;i<arr.length-1;i++){
              if(arr[i]==word[1])
                {
                  if(i==0){
                        temp3=word[0]+"-";
                      }
                    for(i=1;i<word.length;i++){
                      temp3=temp3+word[i];
                    }
                return temp3;
              } 
          }
      }
    
      else{
          return word;
      }
    }
    else if(code=="en" || code == "en-US" || code == "en-latn" ||code=="en-IE"){
      return word;
    }
    
    else if(code == "el"){
            temp1=""
            if (word[word.length-1] == '\u03A3'){
              for(i=0;i<word.length;i++)
                if(i!=word.length-1)
                  temp1+=word[i]
              temp1=temp1+'\u03c2';
              return temp1;
            }
    else if(code=="zh" || code == "th"){
            temp2=word;
        console.log(temp2);
    }
    else{
      return word;
    }
  }
}
let a =my_name("tr","KASIM");
console.log(a.toLocaleLowerCase());
let b = my_name("el","ΠΌΛΗΣ");
console.log(b.toLocaleLowerCase());
let c=my_name('ga',"tAcht");
console.log(c.toLocaleLowerCase());
let d=my_name("ga","TACHT");
console.log(d.toLocaleLowerCase());
let e=my_name("en","HELLO");
console.log(e.toLocaleLowerCase());
let f= my_name("ga","nATHAIR");
console.log(f.toLocaleLowerCase());
let g=my_name("ga","nAthair");
console.log(g.toLocaleLowerCase());
let h =my_name("en-latn","---OK");
console.log(h.toLocaleLowerCase());
let j =my_name("en-IE","cAmEl");
console.log(j.toLocaleLowerCase());