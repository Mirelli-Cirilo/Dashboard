function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}

function total_vendido(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('faturamento_total').innerHTML = data.total
    })

}

function despesa_anual(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('despesa_anual').innerHTML = data.despesa_anual.toFixed(3)
    })

}

function lucro_liquido(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('lucro_liquido').innerHTML = data.lucro.toFixed()
    })

}

function despesa_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const context = document.getElementById('despesas_mensais').getContext('2d');
        const myChart = new Chart(context, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Despesas',
                    data: data.data,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                }]
            },
            
        });

    })
}

function faturamento_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const context = document.getElementById('faturamento_mensal').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(context, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Faturamento Mensal',
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 1
                }]
            },
            
        });

    })

}

function produtos_mais_vendidos(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const context = document.getElementById('produtos_mais_vendidos').getContext('2d');
        var cores_produtos_mais_vendidos = gera_cor(qtd=4)
        const myChart = new Chart(context, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Faturamento',
                    data: data.data,
                    backgroundColor: cores_produtos_mais_vendidos[0],
                    borderColor: cores_produtos_mais_vendidos[1],
                    borderWidth: 1
                }]
            },
            
        });


    })
  
}

function funcionario_mes(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const context = document.getElementById('funcionarios_do_mes').getContext('2d');
        var cores_funcionarios_do_mes = gera_cor(qtd=3)
        const myChart = new Chart(context, {
            type: 'polarArea',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Funcionário do mês',
                    data: data.data,
                    backgroundColor: cores_funcionarios_do_mes[0],
                    borderColor: cores_funcionarios_do_mes[1],
                    borderWidth: 1
                }]
            },
        });
    })
}