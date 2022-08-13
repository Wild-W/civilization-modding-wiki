---
tags:
- RequirementType
title: REQUIREMENT_COLLECTION_ALL_MET
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COLLECTION_ALL_MET
>
> * Class: `ANY`
> * Arguments:
>	* RequirementSetId `String`
>	* CollectionType `String`

## Samples

```SQL {title="CULTURE_VICTORY_PER_MEMBER_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"CULTURE_VICTORY_PER_MEMBER_REQUIREMENT",
		"REQUIREMENT_COLLECTION_ALL_MET"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"CULTURE_VICTORY_PER_MEMBER_REQUIREMENT",
		"CollectionType",
		"COLLECTION_MAJOR_OPPOSING_PLAYERS"
	),
	(
		"CULTURE_VICTORY_PER_MEMBER_REQUIREMENT",
		"RequirementSetId",
		"CULTURE_VICTORY_ENOUGH_TOURISTS_REQUIREMENTS"
	);
	```
