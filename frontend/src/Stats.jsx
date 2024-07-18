import React from 'react'

const Statistics = ({stats}) => {
    return <div>
        <table className='stats'>
            <tbody>
                <tr>
                    <td>Total Documents ({stats.totalDocuments})</td>
                    <td>In Draft ({stats.inDraft})</td>
                    <td>In Review ({stats.inReview})</td>
                    <td>Pending Approval ({stats.pendingApproval})</td>
                    <td>Complete ({stats.complete})</td>
                </tr>
            </tbody>
        </table>
    </div>
}

export default Statistics