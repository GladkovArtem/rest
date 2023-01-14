import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data
                    this.setState(
                        {
                            'authors': authors
                        }
                    )
            }).catch(error => console.log(error))
    }
//    componentDidMount() {
//        const authors = [
//            {
//                'id': '3beeb1f1-2ec2-475e-bd38-4952f2e4235b',
//                'first_name': 'Фёдор',
//                'last_name': 'Достоевский',
//                'email': 'react@gb.com',
//                'user_name': 'react'
//            },
//            {
//                'id': '2831e77b-463d-4678-b261-cb52684db28a',
//                'first_name': 'Фёдор',
//                'last_name': 'Достоевский2',
//                'email': 'react@gb.ru',
//                'user_name': 'rest'
//            },
//        ]
//        this.setState(
//            {
//                'authors': authors
//            }
//        )
//    }

    render () {
        return (
            <div>
                <AuthorList authors={this.state.authors} />
            </div>
        )
    }
}

export default App;
