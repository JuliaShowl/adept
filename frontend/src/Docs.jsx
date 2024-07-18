import React from 'react'

const Docs = ({docs, updateStatus}) => {
    return <div data-testid='docs-component'>
        <table className='docs'>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Status</th>
                    <th>Last Edited</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {docs.map((doc) => (
                    <tr key={doc.id}>
                        <td>{doc.name}</td>
                        <td>{doc.status}</td>
                        <td>{doc.lastEdited}</td>
                        <td><button onClick={() => updateStatus(doc)}>Update Status</button></td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
       
}

export default Docs