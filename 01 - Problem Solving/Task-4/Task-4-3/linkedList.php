<?php

class Node {
  public $data;
  public $next;
  public function __construct($data) {
    $this->data = $data;
    $this->next = null;
  }
  function read() {
    return $this->data;
  }
}

class LinkedList {
  private $fNode;
  private $lNode;
  public $length;

  public function __construct() {
    $this->fNode = NULL;
    $this->lNode = NULL;
    $this->length = 0;
  }

  public function insertAtFirst($data) {
    $linked = new Node($data);
    $linked->next = $this->fNode;
    $this->fNode = $linked;
    if ($this->lNode == NULL) {
      $this->lNode = $linked;
    }
    $this->length++;
  }

  public function insert($item, $key) {
    if ($key == 0) {
      $this->insertAtFirst($item);
    } else {
      $linked = new Node($item);
      $current = $this->fNode;
      $previous = $this->fNode;
      for ($i = 0; $i < $key; $i++) {
        $previous = $current;
        $current = $current->next;
      }
      $previous->next = $linked;
      $linked->next = $current;
    }
    $this->length++;
  }

  public function pList() { // print
    $listData = [];
    $current = $this->fNode;
    while ($current != NULL) {
      array_push($listData, $current->read());
      $current = $current->next;
    }
    foreach ($listData as $item) {
      echo $item . " ";
    }
  }

  public function deleteItem($key) {
    $current = $this->fNode;
    $previous = $this->lNode;
    while($current->data != $key) {
      if ($current->next == null) {
        return null;
      } else {
        $previous = $current;
        $current = $current->next;
      }
    }
    if ($current == $this->fNode) {
      if ($this->length == 1) {
        $this->lNode = $this->fNode;
      }
      $this->fNode = $this->fNode->next;
    } else {
      if ($this->lNode == $current) {
        $this->lNode = $previous;
      }
      $previous->next = $current->next;
    }
    $this->length--;
  }

}

$l = new LinkedList();
$l->insertAtFirst("01");
$l->insertAtFirst("02");
$l->insertAtFirst("03");
$l->insert("04", 2);
$l->pList();

echo " - items: " . $l->length; // count list