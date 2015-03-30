<?php
class OpCacheDataModel
{
        public function getStatusDataRows(){
        $stats = opcache_get_status();
        foreach ($stats as $key=>$val) {
                if (is_array($val)) {
                        foreach ($val as $k=>$v) {
                        echo $k;
                        echo ':';
                        echo $v;
                        echo ';';
                        }
                }
        }}
}
$dataModel = new OpCacheDataModel();

echo $dataModel->getStatusDataRows();
?>

