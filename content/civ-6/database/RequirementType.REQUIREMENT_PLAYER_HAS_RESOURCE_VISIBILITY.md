---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_RESOURCE_VISIBILITY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_RESOURCE_VISIBILITY
>
> * Class: `PLAYERS`
> * Arguments:
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples

```SQL {title="REQUIRES_PLAYER_CAN_SEE_ALUMINUM"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_CAN_SEE_ALUMINUM",
		"REQUIREMENT_PLAYER_HAS_RESOURCE_VISIBILITY"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_CAN_SEE_ALUMINUM",
		"ResourceType",
		"RESOURCE_ALUMINUM"
	);
	
```
