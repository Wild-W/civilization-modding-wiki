---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_SHARING_INFO
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_SHARING_INFO
>
> * Class: `PLAYERS`
> * Arguments:
>	* SharingInfoWell `Boolean`

## Samples

```SQL {title="REQUIRES_NOT_SHARING_INFO"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_NOT_SHARING_INFO",
		"REQUIREMENT_PLAYER_IS_SHARING_INFO"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_NOT_SHARING_INFO",
		"SharingInfoWell",
		0
	);
	
```
