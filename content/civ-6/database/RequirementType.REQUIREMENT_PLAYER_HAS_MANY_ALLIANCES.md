---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_MANY_ALLIANCES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_MANY_ALLIANCES
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinOwnerAlliances `Integer`
>	* ChecKForFewer `Boolean`

## Samples

```SQL {title="REQUIRES_HAS_FEW_ALLIANCES"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_FEW_ALLIANCES",
		"REQUIREMENT_PLAYER_HAS_MANY_ALLIANCES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_FEW_ALLIANCES",
		"ChecKForFewer",
		1
	),
	(
		"REQUIRES_HAS_FEW_ALLIANCES",
		"MinOwnerAlliances",
		1
	);
	```
