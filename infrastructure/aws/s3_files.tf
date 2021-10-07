# Faz o upload do arquivo para o s3
# resource "aws_s3_bucket_object" "JobSpark" {
#   bucket = aws_s3_bucket.dl.id
#   key    = "emr-code/pyspark/JobSpark.py"
#   acl    = "private"
#   source = "../etl/JobSpark.py"
#   etag   = filemd5("../etl/JobSpark.py")
# }