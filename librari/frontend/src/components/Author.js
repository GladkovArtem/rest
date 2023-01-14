import React from 'react'


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.id}
            </td>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.email}
            </td><td>
                {author.user_name}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                Id
            </th>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Email
            </th>
            <th>
                User Name
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}


export default AuthorList
