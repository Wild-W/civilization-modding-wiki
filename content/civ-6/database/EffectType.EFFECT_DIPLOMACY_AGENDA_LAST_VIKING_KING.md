---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_LAST_VIKING_KING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_LAST_VIKING_KING
>
> * Class: `PLAYERS`
> * Parameters:
>	* BetterMilitaryBonus `Integer`
>	* HiddenAgenda `Boolean`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`
>	* TopMilitaryBonus `Integer`

## Samples
```SQL {title="AGENDA_GREAT_WHITE_FLEET"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_GREAT_WHITE_FLEET",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_LAST_VIKING_KING",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_GREAT_WHITE_FLEET",
		"BetterMilitaryBonus",
		4
	),
	(
		"AGENDA_GREAT_WHITE_FLEET",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_GREAT_WHITE_FLEET",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_DESCRIPTION_GREAT_WHITE_FLEET"
	),
	(
		"AGENDA_GREAT_WHITE_FLEET",
		"StatementKey",
		"AGENDA_GREAT_WHITE_FLEET_WARNING"
	),
	(
		"AGENDA_GREAT_WHITE_FLEET",
		"TopMilitaryBonus",
		6
	);
	
```

```SQL {title="AGENDA_LAST_VIKING_KING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_LAST_VIKING_KING",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_LAST_VIKING_KING",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_LAST_VIKING_KING",
		"StatementKey",
		"AGENDA_LAST_VIKING_KING_WARNING"
	);
	
```

