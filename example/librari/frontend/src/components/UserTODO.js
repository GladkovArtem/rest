import React from 'react'
import {useParams} from 'react-router-dom'

const TODOItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.project.project_name}
            </td>
            <td>
                {item.text}
            </td>
            <td>
                {item.create_date}
            </td>
            <td>
                {item.update_date}
            </td>
            <td>
                {item.author.user_name}
            </td>
            <td>
                {item.is_active}
            </td>
        </tr>
    )
}


const UserTODOList = ({items}) => {
    let {id} = useParams()
    let filtered_items = items.filter((item) => item.author.id = id)
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Create date
            </th>
            <th>
                Update date
            </th>
            <th>
                User Name
            </th>
            <th>
                Is active
            </th>
            {filtered_items.map((item) => <TODOItem item={item} />)}
        </table>
    )
}


export default UserTODOList
