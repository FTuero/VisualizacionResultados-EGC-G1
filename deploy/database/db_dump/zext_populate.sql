USE `votaciones_splc`;

#Question_optionEXT

INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (101, 'option2', 50);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (102, 'option3', 50);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (103, 'option2', 29);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (104, 'option2', 36);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (105, 'option2', 6);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (106, 'option2', 45);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (107, 'option3', 45);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (108, 'option2', 10);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (109, 'option2', 37);
INSERT INTO question_option (`id`, `description`, `question_id`) VALUES (110, 'option3', 37);


#VoteEXT


INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (301, '1dfd338fdd03b69456i40e692c81cb88562830835a8cb7bd4a04bb8dcb9abb84', 1, '2018-05-15');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (302, 'b7f1f52dbd312ac66d440283dadoc4he633abe4363b186d9a8d8c2cd5472c932', 1, '2018-05-17');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (303, '1dfd338fdd03b69456i40e692c81cb88562830835a8cb7bd4a04bb8dcb9abb84', 2, '2018-05-16');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (304, 'b7f1f52dbd312ae4363b186d9c66d440283dadoc4he633aba8d8c2cd5472c932', 2, '2018-05-18');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (305, '1dfd338fdd03b69456ib88562830835a40e692c8cb7bd4a04bb8dcb81c9abb84', 3, '2018-05-22');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (306, 'b7f1f5adoc4he633abe2dbd31a8d8c2cd5472c92ac66d440283d4363b186d932', 3, '2018-05-24');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (307, '1dfd338fdd03b69e692c81cba488562830835a8cb7bd456i4004bb8dcb9abb84', 1, '2018-05-21');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (308, 'b7f1f83dadoc4he633abe4352dbd312ac66d440263b186d9a8d8c2cd5472c932', 1, '2018-05-27');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (309, '1dfd33i40e692c81cb885628fdd03b69456830835a8cb7bd4a04bb8dcb9abb84', 3, '2018-05-29');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (310, '44063b7f1f52dbd312283dadoc4heac66d3abe4363b186d9a8d8c2cd5472c932', 3, '2018-05-26');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (311, '1df7bd4a04bb8dcb969456i40e692cd338fdd03ba8cb81cb88562830835abb84', 1, '2018-06-02');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (312, 'b7f183dadoc4hf5ac66d442dbd312abe436302e633b1d8c2cd5472c9386d9a82', 1, '2018-06-04');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (313, '1dfd338fdd03b69456i40e692bd4a04bb8c81cb8857dcb9abb8462830835a8cb', 2, '2018-06-01');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (314, 'b7f1f5263b186d9dbd312ae4383dadoc66d44he633a402cba8d8c2cd5472c932', 2, '2018-06-05');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (315, '1dfd338fdd03b69456ib8856e692c8cb7bd4a0483083bb8dcb81c9a25a40bb84', 3, '2018-06-12');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (316, '8c2cd54b7f3abe21f5adoc4he63dbd31a8d72c92ac66d440283d4363b186d932', 3, '2018-06-14');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (317, '1dfd338fdd03b6908356i4004e692c81cba4885a8cb7bd456283bb8dcb9abb84', 1, '2018-06-11');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (318, 'b7f1f83dadoc4he633abe435202cd54dbd31263b186d9a8d8c2ac66d4472c932', 1, '2018-06-09');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (319, '1dfd81cb885633i40e6dd03b69456830835a8c92c28fb7bd4a04bb8dcb9abb84', 3, '2018-06-13');
INSERT INTO vote (`id`, `token`, `vote_type_id`, `vote_date`) VALUES (320, '440283dadoc4he633abe4363b7f1f52dbd312ac6472c96db186d9a8d8c2cd532', 3, '2018-06-07');

#OptionPerVoteEXT


INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (401, 301, 12);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (402, 302, 101);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (403, 303, 56);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (404, 304, 103);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (405, 305, 105);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (406, 306, 105);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (407, 307, 107);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (408, 308, 107);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (409, 309, 73);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (410, 310, 108);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (411, 311, 109);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (412, 312, 109);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (413, 313, 110);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (414, 314, 110);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (415, 315, 104);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (416, 316, 106);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (417, 317, 12);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (418, 318, 103);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (419, 319, 12);
INSERT INTO option_per_vote (`id`, `vote_id`, `question_option_id`) VALUES (420, 320, 103);

