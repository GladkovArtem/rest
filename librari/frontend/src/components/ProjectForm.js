import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {project_name: '', link: '', authors: props.authors[0]?.id}
    }

    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createProject(this.state.project_name, this.state.link, this.state.authors)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)} >
                <div className="form-group">
                    <label for="project_name">project_name</label>
                    <input type="text" className="form-control" name="project_name" value={this.state.project_name} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="link">link</label>
                    <input type="text" className="form-control" name="link" value={this.state.link} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="authors">user</label>

                    <select name="authors" className='from-control' onChange={(event)=>this.handleChange(event)}>
                        {this.props.authors.map((author)=><option value={author.id}>{author.user_name}</option>)}
                    </select>

                </div>
            <input type="submit" className="btn btn-primary" value="Save" />
        </form>
        );
    }
}

export default ProjectForm