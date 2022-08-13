---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_TYPE_MATCHES
>
> * Class: `PLAYERS`
> * Arguments:
>	* CivilizationType `String`

## Samples

```SQL {title="PLAYER_IS_MAYA"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLAYER_IS_MAYA",
		"REQUIREMENT_PLAYER_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLAYER_IS_MAYA",
		"CivilizationType",
		"CIVILIZATION_MAYA"
	);
	
```
