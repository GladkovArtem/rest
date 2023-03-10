import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import ProjectList from './components/Project.js'
import TODOList from './components/Todos.js'
import  UserTODOList from './components/UserTODO.js'
import axios from 'axios'
import {BrowserRouter, HashRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import LoginForm from './components/Auth.js'
import ProjectForm from './components/ProjectForm.js'
import Cookies from 'universal-cookie';

const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу `{location.pathname}` не найдена</h1>
        </div>
    )
}


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }

    set_token(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        //localStorage.setItem('token', token)
        this.setState({'token':token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        //const token = localStorage.getItem('token')
        this.setState({'token':token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])

            }).catch(error => alert('Неверный пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json',
        }
        if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    createProject(project_name,link, authors){
        const headers = this.get_headers()
        const data = {project_name: project_name,link: link, authors: authors}
        axios.post('http://127.0.0.1:8000/api/projects', data, {headers})
            .then(response => {
                let new_project = response.data
                const authors = this.state.authors.filter((author)=> author.id === new_project.authors)[0]
                new_project.authors = authors
                this.setState({projects:[...this.state.projects, new_project]})
            }).catch(error => console.log(error))
    }

    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`,{headers})
            .then(response => {
                this.setState({projects: this.state.projects.filter((project)=> project.id !== id)})
            }).catch(error => console.log(error))
    }

    deleteTODO(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todos/${id}`,{headers})
            .then(response => {
                this.setState({todos: this.state.todos.filter((item)=> item.id !== id)})
            }).catch(error => console.log(error))
    }

    load_data () {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors', {headers})
            .then(response => {
                const authors = response.data.results
                    this.setState(
                        {
                            'authors': authors
                        }
                    )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data.results
                    this.setState(
                        {
                            'projects': projects
                        }
                    )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos', {headers})
            .then(response => {
                const todos = response.data.results
                    this.setState(
                        {
                            'todos': todos
                        }
                    )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
   }


    render () {
        return (
            <div className='App'>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                 <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                 <Link to='/todos'>Todos</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                        <Route exact path='/projects/create' component={() => <ProjectForm authors={this.state.authors} createProject={(project_name,link, authors)=> this.createProject(project_name,link, authors)} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} deleteProject={(id)=>this.deleteProject(id)}/>} />
                        <Route exact path='/todos' component={() => <TODOList items={this.state.todos} deleteTODO={(id)=>this.deleteTODO(id)}/>} />
                        <Route exact path='/author/:id' component={() => <UserTODOList items={this.state.todos} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)}/>} />
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>
        )
    }
}

export default App;
