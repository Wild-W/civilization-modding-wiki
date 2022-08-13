---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_RESOURCE_IMPROVED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_RESOURCE_IMPROVED
>
> * Class: `PLAYERS`
> * Arguments:
>	* ResourceType `String`

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_NO_IMPROVED_ALUMINUM"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_NO_IMPROVED_ALUMINUM",
		"REQUIREMENT_PLAYER_HAS_RESOURCE_IMPROVED",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_NO_IMPROVED_ALUMINUM",
		"ResourceType",
		"RESOURCE_ALUMINUM"
	);
	```
