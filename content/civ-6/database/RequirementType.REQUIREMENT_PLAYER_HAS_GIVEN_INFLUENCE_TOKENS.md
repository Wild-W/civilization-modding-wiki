---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_GIVEN_INFLUENCE_TOKENS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_GIVEN_INFLUENCE_TOKENS
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinimumTokens `Integer`

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_LARGE_INFLUENCE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_LARGE_INFLUENCE",
		"REQUIREMENT_PLAYER_HAS_GIVEN_INFLUENCE_TOKENS"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_LARGE_INFLUENCE",
		"MinimumTokens",
		6
	);
	```
