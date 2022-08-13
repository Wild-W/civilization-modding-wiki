---
tags:
- RequirementType
title: REQUIREMENT_COLLECTION_COUNT_EQUALS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COLLECTION_COUNT_EQUALS
>
> * Class: `ANY`
> * Arguments:
>	* Count `Integer`
>	* CollectionType `String`

## Samples

```SQL {title="DEFAULT_VICTORY_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"DEFAULT_VICTORY_REQUIREMENT",
		"REQUIREMENT_COLLECTION_COUNT_EQUALS"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"DEFAULT_VICTORY_REQUIREMENT",
		"CollectionType",
		"COLLECTION_MAJOR_TEAMS"
	),
	(
		"DEFAULT_VICTORY_REQUIREMENT",
		"Count",
		1
	);
	
```
