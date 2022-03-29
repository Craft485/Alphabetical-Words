import { readFile, writeFile, readdir } from 'fs';

readdir('../datasets', {encoding: 'utf-8'}, (err, files) => {
    if (err) throw err
    
    files.forEach(file => {
        console.info(`Searching "${file}"`)
        const finalWordList = []
        let longestWord = { word: '', length: 0 }

        readFile(`../datasets/${file}`, {encoding: 'utf-8'},  (err, data) => {
            if (err) throw err
            const words = data.split('\n')
        
            words.forEach(word => { 
                word = word.replace(/\r/, '').trim()
                const sortedWord = word.trim().split('').sort().join('')
                if (word === sortedWord) {
                    finalWordList.push(word)
                    if (word.length > longestWord.length) longestWord = { word: word, length: word.length }
                }
            })

            writeFile(`../out/${file.split('.')[0]}.JS.log`, finalWordList.join('\n') + `\n${longestWord.word + ' | ' + longestWord.length}`, (err) => { if (err) throw err })
            console.info(`Showing results for: ${file} \n - # of words searched: ${words.length} | # of alphabetical words: ${finalWordList.length} | Longest Word Data: ${JSON.stringify(longestWord)}`)
        })
    })
})
