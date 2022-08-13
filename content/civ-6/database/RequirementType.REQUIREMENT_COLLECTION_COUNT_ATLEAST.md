---
tags:
- RequirementType
title: REQUIREMENT_COLLECTION_COUNT_ATLEAST
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COLLECTION_COUNT_ATLEAST
>
> * Class: `ANY`
> * Arguments:
>	* Count `Integer`
>	* CollectionType `String`

## Samples

```SQL {title="REQUIRES_CAPITAL_CITY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CAPITAL_CITY",
		"REQUIREMENT_COLLECTION_COUNT_ATLEAST"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CAPITAL_CITY",
		"CollectionType",
		"COLLECTION_PLAYER_CAPITAL_CITY"
	),
	(
		"REQUIRES_CAPITAL_CITY",
		"Count",
		1
	);
	```
