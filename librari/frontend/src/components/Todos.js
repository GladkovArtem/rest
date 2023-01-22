import React from 'react'


const TODOItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.project}
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
                {item.author}
            </td>
            <td>
                {item.is_active}
            </td>
        </tr>
    )
}


const TODOList = ({items}) => {
    return (
        <table>
            <th>
                Project id
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
                User id
            </th>
            <th>
                Close
            </th>
            {items.map((item) => <TODOItem item={item} />)}
        </table>
    )
}


export default TODOList
