resource "aws_glue_catalog_database" "educ_sup" {
    name = "db_educ_sup"
}

resource "aws_glue_crawler" "educ_sup" {
  database_name = aws_glue_catalog_database.educ_sup.name
  name          = "educ_sup_s3_crawler"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://${aws_s3_bucket.dl.id}/staging-zone/educ_sup/"
  }
}