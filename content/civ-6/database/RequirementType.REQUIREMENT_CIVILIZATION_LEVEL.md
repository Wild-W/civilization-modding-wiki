---
tags:
- RequirementType
title: REQUIREMENT_CIVILIZATION_LEVEL
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CIVILIZATION_LEVEL
>
> * Class: `PLAYERS`
> * Arguments:
>	* OpponentCivLevel `String`

## Samples

```SQL {title="REQUIRES_MAJOR_CIV_OPPONENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_MAJOR_CIV_OPPONENT",
		"REQUIREMENT_CIVILIZATION_LEVEL"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_MAJOR_CIV_OPPONENT",
		"OpponentCivLevel",
		"CIVILIZATION_LEVEL_FULL_CIV"
	);
	
```
