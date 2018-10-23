q4 = ('select sp.project_id, sp.project_name, count(*) as pr_count '
      'from `learning.ght.sample_python` sp inner join `ghtorrent-bq.ght.pull_requests` pr '
      'on pr.base_repo_id = sp.project_id '
      'group by sp.project_id, sp.project_name having pr_count >@min_pr_count order by pr_count desc'
      )

q4_params = [
        bigquery.ScalarQueryParameter('min_pr_count', 'INT64', 50)
        #bigquery.ScalarQueryParameter('timerange', 'STRING', '2018-10-01'),
        #bigquery.ScalarQueryParameter('timespan', 'INT64', 24),
        ]
#qf.deletetable('sample_prcounts')
qf.runquery(q4, 'sample_prcounts', q4_params)
