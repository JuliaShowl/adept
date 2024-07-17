import {useState} from 'react'

const UpdateStatus = ({currentDoc = {}, updateCallback}) => {
    const [status, setStatus] = useState(currentDoc.status)

    const onSubmit = async e => {
        e.preventDefault()

        const data = {
           status
        }

        const url = "http://127.0.0.1:5000/documents/" + `${currentDoc.id}`

        const options = {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }

        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200){
            const data = await response.json()
            alert(data.message)
        } else{
            updateCallback()
        }
    }

    return (
    <form onSubmit={onSubmit}>
        <div>
            <label>Choose status:</label>
            <select value={status} onChange={e => setStatus(e.target.value)}>
                <option value="In Draft">In Draft</option>
                <option value="In Review">In Review</option>
                <option value="Pending Approval">Pending Approval</option>
                <option value="Complete">Complete</option>
            </select>
        </div>
        <button type='submit'>Update</button>
    </form>
    );
};

export default UpdateStatus