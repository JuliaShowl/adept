import React from 'react'

const Docs = ({docs}) => {
    return <div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Last Edited</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {docs.map((doc) => (
                    <tr key={doc.id}>
                        <td>{doc.name}</td>
                        <td>{doc.lastEdited}</td>
                        <td>{doc.status}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
       
}

export default Docs