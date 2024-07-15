import { useState } from 'react';
import './App.css';
import './Logo.css';
import './button.css';

function App() {

  const [data, setData] = useState(''); // nome, funcao de atualizacao e valor inicial
  const [bigDogs, setbigDogs] = useState('');
  const [smallDogs, setsmallDogs] = useState('');
  const [result, setResult] = useState('');

  async function handleSubmit(e){
    e.preventDefault(); // previne atualização da pagina ao enviar o formulario
    const response = await fetch('http://localhost:8000/api/submit/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({data, bigDogs, smallDogs}),
    });
    const result = await response.json();
    if(result.melhor_canil === ''){
      alert('Valores não informados ou incorretos!')
      
    }
    else{
      setResult(result);
      setData('');
      setbigDogs('');
      setsmallDogs('');  
      console.log(result);
    }
    
  }
  return (
    <div className="App">

    
    <button class="button" data-text="Awesome">
    <span class="actual-text">&nbsp;Canil&nbsp;Eduardo</span>
    <span aria-hidden="true" class="hover-text">&nbsp;Canil&nbsp;Eduardo</span>
    </button>

    <div className='entradas'>
      <form className='formulario' onSubmit={handleSubmit}>
        <span className='span_dados'>Data 
        <input type='date' value= {data}
        onChange={(e)=> setData(e.target.value)}></input>
        </span>
      
        <span className='span_dados'>Digite a quantidade de cães grandes
          <input value= {bigDogs}
        onChange={(e)=> setbigDogs(e.target.value)}></input>
        </span>

        <span className='span_dados'>Digite a quantidade de cães pequenos 
          <input value= {smallDogs}
        onChange={(e)=> setsmallDogs(e.target.value)}></input>
        </span>

        <button type='submit' className='botao'>Pesquisar</button>
        
      </form>
    
      </div>
      {Object.keys(result).length > 0 && (
        <div className='result'>
        <span> O melhor Canil é: {result.melhor_canil}</span>
        <span>Valor: R${result.valor},00</span>
      </div>
      )}
      
       
    </div>

    
  );
}

export default App;


